from datetime import datetime,timedelta
import pytz
import sqlite3


def retrieve_airports(location):
    # (8, 'Boston', 'USA', '(BOS)') -> ["BOS"]
    return [x.strip("(").strip(")").strip() for x in location[3].split(",")]


def get_flight_duration(flight_date, dep_time, arr_time, dep_tz, arr_tz):
    # It's possible on some very long-haul flights that the arrival time is 
    # slightly after the departure time, but we'll cross that bridge when 
    # we get to it.
    if arr_time < dep_time:
        arrival_date = flight_date + timedelta(days=1)
    else:
        arrival_date = flight_date

    dep_time = datetime(flight_date.year, flight_date.month, flight_date.day, dep_time.hour, dep_time.minute)
    dep_time = dep_tz.localize(dep_time)

    arr_time = datetime(arrival_date.year, arrival_date.month, arrival_date.day, arr_time.hour, arr_time.minute)
    arr_time = arr_tz.localize(arr_time)

    time_delta = arr_time - dep_time

    hours = time_delta.seconds // 3600
    minutes = (time_delta.seconds // 60) % 60

    return f"{hours}h {minutes}m"


def get_flight_search_results(origin, destination, flight_date):
    origin_codes = retrieve_airports(origin)
    destination_codes = retrieve_airports(destination)
    search_results = []
    with sqlite3.connect("travelectable.db") as conn:
        curr = conn.cursor()

        # Get timezones
        curr.execute("""SELECT timezone FROM destinations WHERE id = ?""", (origin[0],))
        row = curr.fetchone()
        origin_tz = row[0]
        origin_tz = pytz.timezone(origin_tz)

        curr.execute(
            """SELECT timezone FROM destinations WHERE id = ?""", (destination[0],)
        )
        row = curr.fetchone()
        destination_tz = row[0]
        destination_tz = pytz.timezone(destination_tz)

        for i in origin_codes:
            for j in destination_codes:
                flight = {}
                flight["origin"] = i
                flight["destination"] = j
                curr.execute(
                    """SELECT id,airline,layover_airports,departure_time,arrival_time, num_stops, price 
                    FROM flight_schedules WHERE origin = ? AND destination = ?""",
                    (i, j),
                )
                rows = curr.fetchall()
                columns = [column[0] for column in curr.description]
                flight_options = [dict(zip(columns, row)) for row in rows]
                for flight_option in flight_options:
                    merged_option = {**flight, **flight_option}

                    merged_option["departure_time"] = datetime.strptime(
                        merged_option["departure_time"], "%H:%M"
                    )

                    merged_option["arrival_time"] = datetime.strptime(
                        merged_option["arrival_time"], "%H:%M"
                    )

                    merged_option["duration"] = get_flight_duration(
                        flight_date,
                        merged_option["departure_time"],
                        merged_option["arrival_time"],
                        origin_tz,
                        destination_tz,
                    )

                    search_results.append(merged_option)

    return search_results
