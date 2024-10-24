import math
import sqlite3


def haversine(lat1, lon1, lat2, lon2):
    # R = 6371  # Radius of the Earth in kilometers
    R = 3959  # Radius of the Earth in miles
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = (
        math.sin(dlat / 2) ** 2
        + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    )
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c
    return int(distance)


# lat1, lon1 = 40.7128, 74.0060  # New York
# lat2, lon2 = 34.0522, 118.2437  # Los Angeles
# print(haversine(lat1, lon1, lat2, lon2))  # Output: approximately 3943.6 km


def fetch_results(db_cursor):
    rows = db_cursor.fetchall()
    columns = [column[0] for column in db_cursor.description]

    for row in rows:
        yield dict(zip(columns, row))


with open("airports.dat", "r") as f:
    airport_lat_longs = {}
    source_data = f.readlines()
    for idx, l in enumerate(source_data):
        data = l.split(",")
        try:
            iata_code = data[4].strip('"')
            if len(iata_code) != 3:
                continue
            airport_lat_longs[data[4].strip('"')] = (float(data[6]), float(data[7]))
        except ValueError:
            print(
                f"Error: could not convert {data[6]} or {data[7]} to float on {data[4]}"
            )

with sqlite3.connect("travelectable.db") as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM flight_schedules")

    key_errors = {}

    for row in fetch_results(cursor):
        origin = row["origin"]
        destination = row["destination"]

        airports = [origin]
        if row["layover_airports"]:
            layovers = row["layover_airports"].strip("(").strip(")").split(",")
            airports.extend(layovers)
        airports.append(destination)

        try:
            airport_distances = []
            for i in range(len(airports) - 1):
                lat1, long1 = airport_lat_longs[airports[i]]
                lat2, long2 = airport_lat_longs[airports[i + 1]]
                airport_distances.append(haversine(lat1, long1, lat2, long2))

            cursor.execute(
                "UPDATE flight_schedules SET distances = ? WHERE id = ?",
                (f'({",".join(str(x) for x in airport_distances)})', row["id"]),
            )
        except KeyError as e:
            key_errors[e.args[0]] = key_errors.get(e.args[0], 0) + 1
            continue

    conn.commit()

print(key_errors)
