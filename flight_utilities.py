import base64
from datetime import datetime, timedelta
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

    dep_time = datetime(
        flight_date.year,
        flight_date.month,
        flight_date.day,
        dep_time.hour,
        dep_time.minute,
    )
    dep_time = dep_tz.localize(dep_time)

    arr_time = datetime(
        arrival_date.year,
        arrival_date.month,
        arrival_date.day,
        arr_time.hour,
        arr_time.minute,
    )
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

                    airline_icon_name = (
                        merged_option["airline"].replace(" ", "_").lower()
                    )
                    with open(
                        f"static/airline_icons/{airline_icon_name}.webp", "rb"
                    ) as f:
                        merged_option["logo"] = base64.b64encode(f.read()).decode()

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


def generate_filters(flight_search_results):
    flight_filters = {
        "stops": {},
        "airlines": {},
        "layover_airports": {},
    }

    for result in flight_search_results:
        flight_filters["stops"][result["num_stops"]] = (
            flight_filters["stops"].get(result["num_stops"], 0) + 1
        )

        flight_filters["airlines"][result["airline"]] = (
            flight_filters["airlines"].get(result["airline"], 0) + 1
        )

        if result["layover_airports"] != "":
            layover_airports = [x.strip() for x in result["layover_airports"].strip('(').strip(')').split(",")]
            for layover_airport in layover_airports:
                flight_filters["layover_airports"][layover_airport] = (
                    flight_filters["layover_airports"].get(layover_airport, 0) + 1
                )
                
    return flight_filters
