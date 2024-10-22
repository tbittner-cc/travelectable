import math
import sqlite3

def haversine(lat1, lon1, lat2, lon2):
    #R = 6371  # Radius of the Earth in kilometers
    R = 3959  # Radius of the Earth in miles
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    distance = R * c
    return int(distance)

#lat1, lon1 = 40.7128, 74.0060  # New York
#lat2, lon2 = 34.0522, 118.2437  # Los Angeles
#print(haversine(lat1, lon1, lat2, lon2))  # Output: approximately 3943.6 km

def fetch_results(db_cursor):
    while True:
        row = db_cursor.fetchone()
        if row is None:
            break
        yield row

with sqlite3.connect("travelectable.db") as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM flight_schedules limit 10")

    for row in fetch_results(cursor):
        print(row)