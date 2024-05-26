from datetime import timedelta
import itertools
import json,os,re
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

# Suggest a date range in two weeks in the future for searching.
def get_suggested_dates(current_date):
    suggested_start_date = current_date + timedelta(weeks=2)
    suggested_end_date = suggested_start_date + timedelta(days = 6)

    if (suggested_start_date.month == suggested_end_date.month):
        suggested_date_range = "{}-{}".format(suggested_start_date.strftime("%B %-d"), suggested_end_date.strftime("%-d"))
    else:
        suggested_date_range = "{}-{}".format(suggested_start_date.strftime("%B %-d"), suggested_end_date.strftime("%B %-d"))

    return suggested_date_range

def get_hotel_offers():
    with open(os.path.join(os.path.dirname(__file__), "offers_test.txt"), "r") as file:
        offer_details = file.read()
    return get_list_of_dicts(offer_details)

def get_hotel_details():
    with open(os.path.join(os.path.dirname(__file__), "hotel_details.txt"), "r") as file:
        hotel_details = file.read()
    return get_list_of_dicts(hotel_details)

def get_list_of_dicts(list_of_dicts_str):
    list_of_dicts_str = list_of_dicts_str.replace('$', '')

    start_index = list_of_dicts_str.find('[')
    end_index = list_of_dicts_str.rfind(']')
    list_of_dicts_str = list_of_dicts_str[start_index:end_index+1]

    list_of_dicts = json.loads(list_of_dicts_str)

    return list_of_dicts

def build_sublist(src_list,list_size):
    return [src_list[i:i + list_size] for i in range(0, len(src_list), list_size)]

def merge_sublists(src_list):
    return list(itertools.chain.from_iterable(src_list))

def execute_llm_query(query,max_tokens = 512):
    data = replicate.run(
        "meta/meta-llama-3-70b-instruct",
         input={"prompt": query, "max_tokens": max_tokens})
    
    return "".join(data)