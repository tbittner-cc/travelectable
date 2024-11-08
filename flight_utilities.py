import base64
from datetime import datetime, timedelta
import pytz
import random
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


def get_all_flight_search_results(origin, destination, flight_date):
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
            layover_airports = [
                x.strip()
                for x in result["layover_airports"].strip("(").strip(")").split(",")
            ]
            for layover_airport in layover_airports:
                flight_filters["layover_airports"][layover_airport] = (
                    flight_filters["layover_airports"].get(layover_airport, 0) + 1
                )

    return flight_filters


def _time_flight_filter(flight_results, flight_filters, time_key):
    times = [key.split("-")[0] for key in flight_filters if time_key in key]

    if times == []:
        time_results = flight_results
    else:
        time_results = []
        if "morning" in times:
            morning_results = [
                result
                for result in flight_results
                if result[f"{ time_key }_time"].hour > 4
                and result[f"{ time_key }_time"].hour < 12
            ]
        else:
            morning_results = []
        time_results.extend(morning_results)

        if "afternoon" in times:
            afternoon_results = [
                result
                for result in flight_results
                if result[f"{ time_key }_time"].hour > 11
                and result[f"{ time_key }_time"].hour < 18
            ]
        else:
            afternoon_results = []
        time_results.extend(afternoon_results)

        if "evening" in times:
            evening_results = [
                result
                for result in flight_results
                if result[f"{ time_key }_time"].hour > 17
            ]
        else:
            evening_results = []
        time_results.extend(evening_results)

    return time_results


def filter_flights(flight_filters, flight_search_results):
    # If there are no filters, return everything
    if flight_filters == {}:
        return flight_search_results

    stops = [int(key.split("-")[0]) for key in flight_filters if "stop" in key]
    # If no stop filters, return all stop combinations
    if stops == []:
        stop_results = flight_search_results
    else:
        stop_results = [
            result for result in flight_search_results if result["num_stops"] in stops
        ]

    airlines = [key.split("-")[1] for key in flight_filters if "airline" in key]

    if airlines == []:
        airline_results = stop_results
    else:
        airline_results = [
            result for result in stop_results if result["airline"] in airlines
        ]

    layover_airports = [key.split("-")[1] for key in flight_filters if "airport" in key]

    if layover_airports == []:
        layover_results = airline_results
    else:
        layover_results = [
            result
            for result in airline_results
            if any(s in result["layover_airports"] for s in layover_airports)
        ]

    departure_results = _time_flight_filter(
        layover_results, flight_filters, "departure"
    )

    arrival_results = _time_flight_filter(departure_results, flight_filters, "arrival")

    return arrival_results


def get_flight_details(flight_id, flight_date):
    with sqlite3.connect("travelectable.db") as conn:
        curr = conn.cursor()
        curr.execute(
            """SELECT id,origin,destination,airline,departure_time,arrival_time,price,num_stops,layover_airports,distances
            FROM flight_schedules WHERE id = ?""",
            (flight_id,),
        )
        rows = curr.fetchone()

        columns = [column[0] for column in curr.description]
        flight_details = dict(zip(columns, rows))

        flight_details["departure_time"] = datetime.strptime(
            flight_details["departure_time"], "%H:%M"
        )

        flight_details["arrival_time"] = datetime.strptime(
            flight_details["arrival_time"], "%H:%M"
        )

        flight_details["distances"] = [
            int(x) for x in flight_details["distances"].strip("(").strip(")").split(",")
        ]

        flight_pairs = (
            [flight_details["origin"]]
            + [
                x
                for x in flight_details["layover_airports"]
                .strip("(")
                .strip(")")
                .split(",") if x != ""
            ]
            + [flight_details["destination"]]
        )

        flight_details['flight_pairs'] = flight_pairs

    return flight_details


def _get_seats_for_flight_class(flight_class, row_offset=0):
    seat_letters = {i: chr(64 + i) for i in range(1, 27)}
    seat_list = []
    for i in range(1, flight_class[-1] + 1):
        aisle_offset = 0
        aisle_list = []
        for j in flight_class[:-1]:
            sub_aisle_list = []
            if j == 0:
                continue
            for k in range(aisle_offset + 1, aisle_offset + j + 1):
                sub_aisle_list.append(f"{i+row_offset}{seat_letters[k]}")
            aisle_offset += j
            aisle_list.append(sub_aisle_list)
            aisle_list.append([])
        seat_list.append(aisle_list[:-1])

    return seat_list


def get_flight_seat_configuration(distance):
    with sqlite3.connect("travelectable.db") as conn:
        curr = conn.cursor()
        curr.execute(
            """SELECT * FROM airplanes""",
        )
        rows = curr.fetchall()

        columns = [column[0] for column in curr.description]
        airplanes = [dict(zip(columns, row)) for row in rows]

    airplanes = sorted(airplanes, key=lambda airplane: airplane["range"])
    eligible_airplanes = [
        airplane for airplane in airplanes if airplane["range"] >= distance
    ]

    # Choose randomly from eligible planes with the same distance capability
    if not eligible_airplanes:
        # Get the one with the longest range
        airplane = random.choice([airplanes[-1], airplanes[-2]])
    else:
        airplane = random.choice([eligible_airplanes[0], eligible_airplanes[1]])

    all_seats = {"first_class": [], "economy_class": []}

    raw_seat_configuration = [
        tuple(map(int, x.split("-")))
        for x in airplane["seat_configuration"].strip("(").strip(")").split(",")
    ]

    if len(raw_seat_configuration) > 1:
        all_seats["first_class"] = _get_seats_for_flight_class(
            raw_seat_configuration[0]
        )

    all_seats["economy_class"] = _get_seats_for_flight_class(
        raw_seat_configuration[-1], len(all_seats["first_class"])
    )
    airplane["seat_configuration"] = all_seats

    exit_configuration = [
        int(x)
        for x in airplane["exit_rows"].strip("(").strip(")").split(",")
        if x != ""
    ]
    airplane["exit_rows"] = exit_configuration

    return airplane
