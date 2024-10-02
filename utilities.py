import ast
import base64
from collections import defaultdict
from datetime import timedelta
from functools import reduce
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

def convert_rates_to_usd(lead_rates):
    updated_lead_rates = []
    rates_dict = defaultdict(list)

    for rate in lead_rates:
        rates_dict[rate[0]].append((rate[1],rate[2]))

    for key in rates_dict:
        is_foreign = are_hotel_rates_in_foreign_currency([rate[0] for rate in rates_dict[key]])
        new_hotel_rates = [(key,rate[0]//rate[1]) if is_foreign else (key,rate[0]) for rate in rates_dict[key]]
        updated_lead_rates.extend(new_hotel_rates)

    return updated_lead_rates

def get_lead_rates(hotels, date):
    hotel_ids = [hotel['id'] for hotel in hotels]
    with sqlite3.connect("travelectable.db") as conn:
        curr = conn.cursor()
        query = f"""SELECT rr.hotel_id,rr.winter_rate,rr.summer_rate,d.conversion_rate 
            FROM room_rates rr JOIN hotels h ON rr.hotel_id = h.id JOIN destinations d ON h.location_id = d.id 
            WHERE hotel_id IN ({','.join(['?' for _ in hotel_ids])})"""
        curr.execute(query, hotel_ids)
        rows = curr.fetchall()
        columns = [column[0] for column in curr.description]
        rates = [dict(zip(columns, row)) for row in rows]

    if is_winter_rate(date):
        all_rates = [(rate['hotel_id'], rate['winter_rate'], float(rate['conversion_rate'])) for rate in rates]
    else:
        all_rates = [(rate['hotel_id'], rate['summer_rate'], float(rate['conversion_rate'])) for rate in rates]

    all_rates = sorted(all_rates, key=lambda x: (x[0], int(x[1])))

    # Convert rates to USD as needed
    all_rates = convert_rates_to_usd(all_rates)

    # Return the lowest rate for each hotel
    lead_rate_dict = {}
    for rate in all_rates:
        hotel, lead_rate = rate
        if hotel not in lead_rate_dict:
            lead_rate_dict[hotel] = int(lead_rate)

    for id in hotel_ids:
        if id not in lead_rate_dict:
            lead_rate_dict[id] = 0

    return list(lead_rate_dict.items())

def are_hotel_rates_in_foreign_currency(rates):
    plus_grand_rates = 0
    for rate in rates:
        if int(rate) >= 1000:
            plus_grand_rates += 1
    return plus_grand_rates == 4 or any(int(rate) >= 10000 for rate in rates)

def get_hotel_details(location, dates, hotel_id, is_winter_rate):
    duration = (dates[1] - dates[0]).days

    with sqlite3.connect("travelectable.db") as conn:
        curr = conn.cursor()
        curr.execute("""SELECT conversion_rate FROM destinations WHERE id = ?""", (location[0], ))
        row = curr.fetchone()
        conversion_rate = float(row[0])

    with sqlite3.connect("travelectable.db") as conn:
        curr = conn.cursor()
        curr.execute(
            """SELECT id,room_type,room_description,winter_rate,summer_rate,amenities,cancellation_policy 
            FROM room_rates WHERE hotel_id = ?""", (hotel_id, ))
        rows = curr.fetchall()
        columns = [column[0] for column in curr.description]
        rates = [dict(zip(columns, row)) for row in rows]

    is_winter_rate_convertible = are_hotel_rates_in_foreign_currency([rate['winter_rate'] for rate in rates])
    is_summer_rate_convertible = are_hotel_rates_in_foreign_currency([rate['summer_rate'] for rate in rates])

    for rate in rates:
        amenities = ast.literal_eval(rate['amenities'])
        rate['amenities'] = amenities

        image = return_room_rate_image_path(rate['room_type'])
        with open(f"static/images/room_rates/{image}.png", "rb") as f:
            rate['image'] = base64.b64encode(f.read()).decode()

        rate['is_winter_rate'] = is_winter_rate
        if is_winter_rate_convertible:
            rate['winter_rate'] = int(float(rate['winter_rate']) // conversion_rate)
        if is_summer_rate_convertible:
            rate['summer_rate'] = int(float(rate['summer_rate']) // conversion_rate)
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

def get_hotel_checkout_details(rate_id,dates,is_winter_rate):
    duration = (dates[1] - dates[0]).days
    with sqlite3.connect("travelectable.db") as conn:
        curr = conn.cursor()
        curr.execute("""SELECT summer_rate,winter_rate FROM room_rates WHERE id = ?""", (rate_id, ))
        rows = curr.fetchall()
        hotel_rates = [(row[0], row[1]) for row in rows] 

        is_summer_rate_convertible = are_hotel_rates_in_foreign_currency([rate[0] for rate in hotel_rates])
        is_winter_rate_convertible = are_hotel_rates_in_foreign_currency([rate[1] for rate in hotel_rates])

        curr.execute(
            """SELECT room_type,winter_rate,summer_rate,hotel_id
            FROM room_rates WHERE id = ?""", (rate_id, ))
        row = curr.fetchone()
        columns = [column[0] for column in curr.description]
        rate = dict(zip(columns, row))

        curr.execute(
          """SELECT h.id,h.name,d.conversion_rate FROM hotels h JOIN destinations d ON h.location_id = d.id WHERE h.id = ?""", 
            (rate['hotel_id'], ))
        row = curr.fetchone()
        columns = [column[0] for column in curr.description]
        hotel = dict(zip(columns, row))

        if is_winter_rate_convertible:
            rate['winter_rate'] = int(int(rate['winter_rate']) // float(hotel['conversion_rate']))
        if is_summer_rate_convertible:
            rate['summer_rate'] = int(int(rate['summer_rate']) // float(hotel['conversion_rate']))
        rate['winter_total'] = str(int(rate['winter_rate']) * duration)
        rate['summer_total'] = str(int(rate['summer_rate']) * duration)

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
