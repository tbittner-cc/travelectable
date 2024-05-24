import ast,sqlite3

import replicate

def execute_llm_query(query,max_tokens = 512):
    data = replicate.run(
        "meta/meta-llama-3-70b-instruct",
         input={"prompt": query, "max_tokens": max_tokens})
    
    return "".join(data)

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

    [{"name":<name>,"address":<address>,"distance":<distance>,"star_rating":star_rating, "description":description},...]

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
        description = execute_llm_query(query)
        description = description.strip('[').strip(']')
        with sqlite3.connect('travel_data.db') as conn:
            curr = conn.cursor()
            curr.execute("UPDATE destinations SET description = ? WHERE id = ?", (description,location_id))
            conn.commit()

    if data[2] == '' or data[2] == None or force_flag:
        query = get_location_points_of_interest_query(location_query)
        points_of_interest = execute_llm_query(query)
        points_of_interest = points_of_interest.split('|')
        with sqlite3.connect('travel_data.db') as conn:
            curr = conn.cursor()
            curr.execute("UPDATE destinations SET points_of_interest = ? WHERE id = ?", (str(points_of_interest),location_id))
            conn.commit()

def populate_hotels(location):
    with sqlite3.connect('travel_data.db') as conn:
        curr = conn.cursor()
        curr.execute("SELECT id,name FROM hotels WHERE location_id = ?", (location[0],))
        rows = curr.fetchall()
        # We're gating the number of hotels for each location to 40
        if len(rows) == 40:
            return
        
        hotel_names = [row[1] for row in rows]
        
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
            print(query)
            hotels = execute_llm_query(query,max_tokens = 1024)
            print(hotels)
            hotels = ast.literal_eval(hotels)
            for hotel in hotels:
                if hotel['name'] in hotel_names:
                    continue
                else:
                    new_hotels_found = True
                    new_hotel = (hotel['name'],hotel['address'],hotel['distance'],hotel['star_rating'],hotel['description'],location[0])
                    curr.execute("INSERT INTO hotels VALUES (?,?,?,?,?,?)", new_hotel)
                    conn.commit()
                    hotel_names.append(hotel['name'])

            if new_hotels_found:
                curr.execute("UPDATE destinations SET hotel_retries = 0 WHERE id = ?", (location[0],))
                conn.commit()
                # If we've got 10 total hotels, we're done for now.
                if len(hotel_names) >= 10:
                    return
            
