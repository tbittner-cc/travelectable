from datetime import datetime
import sqlite3


def retrieve_airports(location):
    # (8, 'Boston', 'USA', '(BOS)') -> ["BOS"]
    return [x.strip("(").strip(")").strip() for x in location[3].split(",")]


def get_flight_search_results(origin_codes, destination_codes):
    search_results = []
    with sqlite3.connect("travelectable.db") as conn:
        curr = conn.cursor()
        for i in origin_codes:
            for j in destination_codes:
                flight = {}
                flight["origin"] = i
                flight["destination"] = j
                curr.execute(
                    """SELECT airline,layover_airports,departure_time,arrival_time, num_stops, price 
                    FROM flight_schedules WHERE origin = ? AND destination = ?""",
                    (i, j),
                )
                rows = curr.fetchall()
                columns = [column[0] for column in curr.description]
                flight_options = [dict(zip(columns, row)) for row in rows]
                print(flight_options)
                for flight_option in flight_options:
                    merged_option = {**flight, **flight_option}
                    merged_option['departure_time'] = datetime.strptime(merged_option['departure_time'], '%H:%M')
                    merged_option['arrival_time'] = datetime.strptime(merged_option['arrival_time'], '%H:%M')
                    search_results.append(merged_option) 

    return search_results
