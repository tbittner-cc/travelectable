import ast,sqlite3
import replicate
import utilities

def get_location_description_query(location):
    return f"""
    Write a 100-word marketing description for visiting {location}.  
    
    Format it as [<description>]

    Do not add a summary or disclaimer at the beginning or end of your reply. Do not deviate from the format.
    """

def get_location_points_of_interest_query(location):
    return f"""
    Provide 5 points of interest for {location}  

    Format it as <point_of_interest>|<point_of_interest>|<point_of_interest>|<point_of_interest>|<point_of_interest>

    Do not add a summary or disclaimer at the beginning or end of your reply. Do not deviate from the format.
    """

def get_hotel_query(radius,location,lat,long):
    return f"""
    List 10 hotels within {radius} miles of {location[1]} at lat/long ({lat},{long}).

    Provide their star ratings, addresses, distance in miles from lat/long ({lat},{long}), 
    and a 50-word description of the hotel.  You must provide an answer even if it's an estimate.

    Format the response as:

    [{{"name":<name>,"address":<address>,"distance":<distance>,"star_rating":star_rating, "description":description}},...]

    Do not add a summary or disclaimer at the beginning or end of your reply. Do not deviate from the format.
    """

def get_room_rate_query(location,hotel_name,address):
    return f"""
    For {hotel_name} at {address} in {location[1]}, provide 4 different room offers. Format it as follows:
    [{{"room_type":<room_type>, "room_description":<room_description>,"amenities":[<list_of_amenities>],"winter_rate":<winter_rate>,"summer_rate":<summer_rate>,"cancellation_policy":cancellation_policy}},...]

    Don't worry if the information isn't up-to-date. Provide a best estimate that matches historical information.  
    For the rates, take into account the seasonality of {location[1]} so higher rates aren't present in the off-season.

    Do not add a summary or disclaimer at the beginning or end of your reply. Do not deviate from the format.
    """

def execute_llm_query(query,max_tokens = 512):
    data = replicate.run(
        "meta/meta-llama-3-70b-instruct",
         input={"prompt": query, "max_tokens": max_tokens})
    
    return "".join(data)

def populate_location_description_and_points_of_interest(location_id,location_query,force_flag=False):
    with sqlite3.connect('travel_data.db') as conn:
        curr = conn.cursor()
        curr.execute("SELECT id,description,points_of_interest FROM destinations WHERE id = ?", (location_id,))
        rows = curr.fetchall()
        data = rows[0]

    if data[1] == '' or data[1] == None or force_flag:
        query = get_location_description_query(location_query)
        description = utilities.execute_llm_query(query)
        description = description.strip('[').strip(']')
        with sqlite3.connect('travel_data.db') as conn:
            curr = conn.cursor()
            curr.execute("UPDATE destinations SET description = ? WHERE id = ?", (description,location_id))
            conn.commit()

    if data[2] == '' or data[2] == None or force_flag:
        query = get_location_points_of_interest_query(location_query)
        points_of_interest = utilities.execute_llm_query(query)
        points_of_interest = points_of_interest.split('|')
        with sqlite3.connect('travel_data.db') as conn:
            curr = conn.cursor()
            curr.execute("UPDATE destinations SET points_of_interest = ? WHERE id = ?", 
                         (str(points_of_interest),location_id))
            conn.commit()

def populate_hotels(location):
    with sqlite3.connect('travel_data.db') as conn:
        curr = conn.cursor()
        curr.execute("SELECT id,name,address FROM hotels WHERE location_id = ?", (location[0],))
        rows = curr.fetchall()
        # We're gating the number of hotels for each location to 40
        if len(rows) == 40:
            return
        
        hotel_names = [row[1] for row in rows]
        hotel_addresses = [row[2] for row in rows]
        
        curr.execute("SELECT latitude,longitude,hotel_retries FROM destinations WHERE id = ?", (location[0],))
        data = curr.fetchall()
        (lat, long,hotel_retries) = data[0]

        # We've tried enough times to get 40 hotels.  We'll go with what we have.
        if hotel_retries >= 10:
            return
        
        radii = [5,10,15,20,25,30,35,40]
        new_hotels_found = False

        for radius in radii:
            query = get_hotel_query(radius,location,lat,long)
            hotels = utilities.execute_llm_query(query,max_tokens = 1024)
            hotels = ast.literal_eval(hotels)
            for hotel in hotels:
                # There's no guarantee that everything will be formatted properly, but
                # we can limit the number of duplicates by checking the name and address.
                if hotel['name'] in hotel_names or hotel['address'] in hotel_addresses:
                    continue
                else:
                    new_hotels_found = True
                    new_hotel = (hotel['name'],hotel['address'],hotel['distance'],hotel['star_rating'],
                                 hotel['description'],location[0])
                    curr.execute("INSERT INTO hotels (name,address,distance,star_rating,description,location_id) "
                                 "VALUES (?,?,?,?,?,?)", new_hotel)
                    conn.commit()
                    hotel_names.append(hotel['name'])
                    hotel_addresses.append(hotel['address'])

            if new_hotels_found:
                curr.execute("UPDATE destinations SET hotel_retries = 0 WHERE id = ?", (location[0],))
                conn.commit()
                # If we've got 10 total hotels, we're done for now.
                if len(hotel_names) >= 10:
                    return
                
            hotel_retries += 1
            curr.execute("UPDATE destinations SET hotel_retries = ? WHERE id = ?", (hotel_retries,location[0]))
            conn.commit()
                
def populate_room_rates(hotel,location):
    with sqlite3.connect('travel_data.db') as conn:
        curr = conn.cursor()
        curr.execute("SELECT id FROM room_rates WHERE hotel_id = ?",(hotel[0],))
        rows = curr.fetchall()
        
        # We've already populated room rates for this hotel.
        if len(rows) != 0:
            return
        
        curr = conn.cursor()
        curr.execute("SELECT id,name,address FROM hotels WHERE id = ?",(hotel[0],))
        rows = curr.fetchall()
        
        query = get_room_rate_query(location,rows[0][1],rows[0][2])
        room_rates = utilities.execute_llm_query(query,max_tokens = 1024)

        room_rates = ast.literal_eval(room_rates)
        for room_rate in room_rates:
            new_room_rate = (hotel[0],room_rate['room_type'],room_rate['room_description'],room_rate['winter_rate'],
                             room_rate['summer_rate'],room_rate['cancellation_policy'],str(room_rate['amenities']))
            curr.execute("INSERT INTO room_rates (hotel_id,room_type,room_description,winter_rate,summer_rate,"
                         "cancellation_policy,amenities) VALUES (?,?,?,?,?,?,?)", new_room_rate)
            conn.commit()
