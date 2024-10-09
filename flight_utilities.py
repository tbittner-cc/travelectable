from datetime import datetime
from dateutil import relativedelta
import pytz
import sqlite3


def retrieve_airports(location):
    # (8, 'Boston', 'USA', '(BOS)') -> ["BOS"]
    return [x.strip("(").strip(")").strip() for x in location[3].split(",")]

def format_duration(duration_str):
    #Formats are 
    #2:30:00 OR
    #-1 day, 2:30:00
    tokens = duration_str.split(',')
    if len(tokens) == 1:
        hours = tokens[0].split(':')[0]
        minutes = tokens[0].split(':')[1]
    else:
        hours = tokens[1].split(':')[0]
        minutes = tokens[1].split(':')[1]

    return f"{hours}h {minutes}m"

def get_flight_search_results(origin, destination):
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
                    """SELECT airline,layover_airports,departure_time,arrival_time, num_stops, price 
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

                    merged_option["duration"] = origin_tz.localize(
                        merged_option["arrival_time"], destination_tz
                    ) - origin_tz.localize(merged_option["departure_time"],origin_tz)
                    merged_option["duration"] = format_duration(str(merged_option['duration']))

                    search_results.append(merged_option)

    return search_results
