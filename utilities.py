import ast
import base64
from datetime import timedelta
import dateutil.parser as parser
import random
import sqlite3


def is_winter_rate(date):
    month = date.month
    return month in [11, 12, 1, 2, 3, 4]


def parse_dates(start_date, end_date):
    try:
        start_date = parser.parse(start_date)
    except parser.ParserError:
        start_date = None
    try:
        end_date = parser.parse(end_date)
    except parser.ParserError:
        end_date = None

    return (start_date, end_date)


# Suggest a date range two weeks in the future for searching.
def get_suggested_dates(current_date):
    suggested_start_date = current_date + timedelta(weeks=2)
    suggested_end_date = suggested_start_date + timedelta(days=6)

    return (suggested_start_date, suggested_end_date)


def get_all_locations():
    locations = []
    with sqlite3.connect('travelectable.db') as conn:
        curr = conn.cursor()
        curr.execute("SELECT id,location,country,airports FROM destinations")
        rows = curr.fetchall()
        for row in rows:
            locations.append((row[0], row[1], row[2], row[3]))

    return locations


def get_hotels(location):
    with sqlite3.connect("travelectable.db") as conn:
        curr = conn.cursor()
        curr.execute(
            "SELECT id,name,address,distance,star_rating,description FROM hotels WHERE location_id = ?",
            (location[0], ))
        rows = curr.fetchall()
        columns = [column[0] for column in curr.description]
        hotels = [dict(zip(columns, row)) for row in rows]

        for hotel in hotels:
            image_name = return_hotel_image_path(hotel['name'])
            location_name = return_location_image_path(location[1])
            hotel['location'] = location_name
            with open(f"static/images/{location_name}/{image_name}/ext.png",
                      "rb") as f:
                hotel['image'] = base64.b64encode(f.read()).decode()

            curr.execute(
                """
                SELECT distinct a.amenity FROM amenities a 
                JOIN room_rates_amenities_xref xref ON a.id = xref.amenity_id
                JOIN room_rates rr ON xref.room_rate_id = rr.id
                WHERE rr.hotel_id = ?""", (hotel['id'], ))

            rows = curr.fetchall()
            hotel['amenities'] = set([row[0] for row in rows])

    random.shuffle(hotels)

    return hotels


def get_amenities(location_id):
    with sqlite3.connect("travelectable.db") as conn:
        curr = conn.cursor()
        curr.execute(
            """SELECT amenity FROM amenities a JOIN room_rates_amenities_xref xref ON a.id = xref.amenity_id 
                        JOIN room_rates rr ON xref.room_rate_id = rr.id JOIN hotels h ON rr.hotel_id = h.id 
                        WHERE h.location_id = ?""", (location_id, ))
        rows = curr.fetchall()

    amenities = set()

    for row in rows:
        amenities.add(row[0])

    return sorted(list(amenities))


def get_hotels_with_amenities(location, amenities):
    all_hotels = get_hotels(location)

    if len(amenities) == 0:
        # If nothing's filtered, return all hotels
        return all_hotels

    amenities_set = set(amenities)
    return [
        hotel for hotel in all_hotels
        if amenities_set.issubset(hotel['amenities'])
    ]


def get_lead_rates(hotels, date):
    hotel_ids = [hotel['id'] for hotel in hotels]
    with sqlite3.connect("travelectable.db") as conn:
        curr = conn.cursor()
        query = "SELECT hotel_id,winter_rate,summer_rate FROM room_rates WHERE hotel_id IN ({})"\
            .format(",".join(['?' for _ in hotel_ids]))
        curr.execute(query, hotel_ids)
        rows = curr.fetchall()

    if is_winter_rate(date):
        all_rates = [(row[0], row[1]) for row in rows]
    else:
        all_rates = [(row[0], row[2]) for row in rows]

    all_rates = sorted(all_rates, key=lambda x: (x[0], int(x[1])))

    # Return the lowest rate for each hotel
    lead_rate_dict = {}
    for rate in all_rates:
        first, second = rate
        if first not in lead_rate_dict:
            lead_rate_dict[first] = second

    for id in hotel_ids:
        if id not in lead_rate_dict:
            lead_rate_dict[id] = ''

    return list(lead_rate_dict.items())


def get_hotel_details(location, dates, hotel_id, is_winter_rate):
    duration = (dates[1] - dates[0]).days
    with sqlite3.connect("travelectable.db") as conn:
        curr = conn.cursor()
        curr.execute(
            """SELECT id,room_type,room_description,winter_rate,summer_rate,amenities,cancellation_policy 
            FROM room_rates WHERE hotel_id = ?""", (hotel_id, ))
        rows = curr.fetchall()
        columns = [column[0] for column in curr.description]
        rates = [dict(zip(columns, row)) for row in rows]

    for rate in rates:
        rate['is_winter_rate'] = is_winter_rate
        amenities = ast.literal_eval(rate['amenities'])
        rate['amenities'] = amenities
        image = return_room_rate_image_path(rate['room_type'])
        with open(f"static/images/room_rates/{image}.png", "rb") as f:
            rate['image'] = base64.b64encode(f.read()).decode()
        rate['winter_total'] = str(int(rate['winter_rate']) * int(duration))
        rate['summer_total'] = str(int(rate['summer_rate']) * int(duration))

    curr.execute(
        "SELECT id,name,address,distance,star_rating,description FROM hotels WHERE id = ?",
        (hotel_id, ))
    row = curr.fetchone()
    columns = [column[0] for column in curr.description]
    hotel = dict(zip(columns, row))

    hotel['rates'] = rates

    image_name = return_hotel_image_path(hotel['name'])
    location_name = return_location_image_path(location[1])
    with open(f"static/images/{location_name}/{image_name}/ext.png",
              "rb") as f:
        hotel['ext_image'] = base64.b64encode(f.read()).decode()
    with open(f"static/images/{location_name}/{image_name}/int.png",
              "rb") as f:
        hotel['int_image'] = base64.b64encode(f.read()).decode()
    hotel['location'] = location_name
    hotel['dates'] = dates

    return hotel

def get_hotel_checkout_details(hotel_id,rate_id,dates,is_winter_rate):
    duration = (dates[1] - dates[0]).days
    with sqlite3.connect("travelectable.db") as conn:
        curr = conn.cursor()
        curr.execute(
            """SELECT room_type,winter_rate,summer_rate
            FROM room_rates WHERE id = ?""", (rate_id, ))
        row = curr.fetchone()
        columns = [column[0] for column in curr.description]
        rate = dict(zip(columns, row))
        rate['winter_total'] = str(int(rate['winter_rate']) * duration)
        rate['summer_total'] = str(int(rate['summer_rate']) * duration)

        curr.execute(
          """SELECT id,name FROM hotels WHERE id = ?""", (hotel_id, ))
        row = curr.fetchone()
        columns = [column[0] for column in curr.description]
        hotel = dict(zip(columns, row))

        hotel['rate'] = rate  
        
    return hotel

def get_selected_locations(location_queries, locations):
    selected_locations = []
    location_query_tuple = (location_queries['origin'],
                            location_queries['destination'])
    for i in location_query_tuple:
        if i == '':
            selected_locations.append(i)
        else:
            selected_location = [
                location for location in locations
                if f"{location[1]}, {location[2]} {location[3]}" == i
            ][0]
            selected_locations.append(selected_location)

    return selected_locations


def return_location_image_path(location_name):
    file_path = location_name.replace(' ', '_').replace('.', '').lower()
    return file_path


def return_hotel_image_path(hotel_name):
    file_path = hotel_name.replace(' ', '_').replace('.',
                                                     '').replace('\'',
                                                                 '').lower()
    return file_path


def return_room_rate_image_path(room_type):
    file_path = room_type.replace(' ', '_').replace('.', '').replace(
        '\'', '').replace('/', '-').lower()
    return file_path
