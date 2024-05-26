from datetime import timedelta
import random,sqlite3
import dateutil.parser as parser

import replicate

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
    with sqlite3.connect('travel_data.db') as conn:
        curr = conn.cursor()
        curr.execute("SELECT id,location,city,state,country FROM destinations WHERE country = 'USA'")
        rows = curr.fetchall()
        for row in rows:
            if row[2] != '':
                locations.append((row[0],f"{row[2]}, {row[3]} {row[4]}"))
            else:
                locations.append((row[0],f"{row[1]}, {row[3]} {row[4]}"))

        curr.execute("SELECT id,location,country FROM destinations WHERE country != 'USA'")
        rows = curr.fetchall()
        for row in rows:
            locations.append((row[0],f"{row[1]}, {row[2]}"))

    return locations

def get_hotels(location):
    with sqlite3.connect("travel_data.db") as conn:
        curr = conn.cursor()
        curr.execute("SELECT id,name,address,distance,star_rating,description FROM hotels WHERE location_id = ?",
                     (location[0],))
        rows = curr.fetchall()

        top_hotels = random.sample(rows, 10)
        other_hotels = [row for row in rows if row not in top_hotels]
        random.shuffle(other_hotels)

        return top_hotels + other_hotels

def execute_llm_query(query,max_tokens = 512):
    data = replicate.run(
        "meta/meta-llama-3-70b-instruct",
         input={"prompt": query, "max_tokens": max_tokens})
    
    return "".join(data)