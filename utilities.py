from datetime import timedelta
import dateutil.parser as parser
import random
import sqlite3

def is_winter_rate(date):
    month = parser.parse(date).month
    return month in [11, 12, 1, 2, 3, 4]

def parse_dates(dates):
    (start_date, end_date) = dates.split("-")
    # spaCy ensures that the dash has no spaces between words
    # Check if the first character of end_date is a digit
    # This is to handle the case of "May 1st-7th" or "May 1-7"
    if end_date[0].isdigit():
        end_date = start_date.split()[0] + " " + end_date

    start_date = parser.parse(start_date)
    end_date = parser.parse(end_date)

    start_date = start_date.strftime("%Y-%m-%d")
    end_date = end_date.strftime("%Y-%m-%d")

    return (start_date, end_date)

# Suggest a date range two weeks in the future for searching.
def get_suggested_dates(current_date):
    suggested_start_date = current_date + timedelta(weeks=2)
    suggested_end_date = suggested_start_date + timedelta(days = 6)

    if (suggested_start_date.month == suggested_end_date.month):
        suggested_date_range = "{}-{}".format(suggested_start_date.strftime("%B %-d"), suggested_end_date.strftime("%-d"))
    else:
        suggested_date_range = "{}-{}".format(suggested_start_date.strftime("%B %-d"), suggested_end_date.strftime("%B %-d"))

    return suggested_date_range

def get_all_locations():
    locations = []
    with sqlite3.connect('travelectable.db') as conn:
        curr = conn.cursor()
        curr.execute("SELECT id,location,country FROM destinations")
        rows = curr.fetchall()
        for row in rows:
                locations.append((row[0],row[1],row[2]))

    return locations

def get_hotels(location):
    with sqlite3.connect("travelectable.db") as conn:
        curr = conn.cursor()
        curr.execute("SELECT id,name,address,distance,star_rating,description FROM hotels WHERE location_id = ?",
                     (location[0],))
        rows = curr.fetchall()
        columns = [column[0] for column in curr.description]
        hotels = [dict(zip(columns, row)) for row in rows]
    
    for hotel in hotels:
        image_name = return_hotel_image_path(hotel['name'])
        location_name = return_location_image_path(location[1])
        hotel['image'] = image_name
        hotel['location'] = location_name

    top_hotels = random.sample(hotels, 10)
    other_hotels = [hotel for hotel in hotels if hotel not in top_hotels]
    random.shuffle(other_hotels)

    return top_hotels + other_hotels
    
def get_lead_rates(hotels,date):
    hotel_ids = [hotel['id'] for hotel in hotels]
    with sqlite3.connect("travelectable.db") as conn:
        curr = conn.cursor()
        query = "SELECT hotel_id,winter_rate,summer_rate FROM room_rates WHERE hotel_id IN ({})"\
            .format(",".join(['?' for _ in hotel_ids]))
        curr.execute(query,hotel_ids)
        rows = curr.fetchall()

    if is_winter_rate(date):
        all_rates = [(row[0],row[1]) for row in rows]
    else:
        all_rates = [(row[0],row[2]) for row in rows]

    all_rates = sorted(all_rates, key=lambda x: (x[0],int(x[1])))

    # Return the lowest rate for each hotel
    lead_rate_dict = {}
    for rate in all_rates:
        first,second = rate 
        if first not in lead_rate_dict:
            lead_rate_dict[first] = second

    for id in hotel_ids:
        if id not in lead_rate_dict:
            lead_rate_dict[id] = ''

    return list(lead_rate_dict.items())

def get_selected_locations(location_queries,locations):
    selected_locations = []
    location_query_tuple = (location_queries['origin'],location_queries['destination'])
    for i in location_query_tuple:
        if i == '':
            selected_locations.append(i)
        else:
            selected_location = [location for location in locations if f"{location[1]}, {location[2]}" == i][0]
            selected_locations.append(selected_location)

    return selected_locations

def return_location_image_path(location_name):
    file_path = location_name.replace(' ','_').replace('.','').lower()
    return file_path

def return_hotel_image_path(hotel_name):
    file_path = hotel_name.replace(' ','_').replace('.','').replace('\'','').lower()
    return file_path

def return_room_rate_image_path(room_type):
    file_path = room_type.replace(' ','_').replace('.','').replace('\'','').replace('/','-').lower()
    return file_path
