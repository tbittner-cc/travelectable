from datetime import datetime
import re,sqlite3

import spacy
from spacy.matcher import Matcher

import utilities

nlp = spacy.load("en_core_web_sm")
matcher = Matcher(nlp.vocab)

months = ["january", "february", "march", "april", 
        "may", "june", "july", "august", 
        "september", "october", "november", "december",
        "jan", "feb", "mar", "apr", 
        "may", "jun", "jul", "aug", 
        "sep", "oct", "nov", "dec"]

date_patterns = [
    [{"LOWER": {"IN": months}},{"IS_DIGIT": True},{"OP": "?", "IS_PUNCT": True},{"OP": "?", "IS_DIGIT": True},
     
     {"OP": "?", "IS_PUNCT": True}, {"OP": "?", "LOWER": "to"},
     
     {"OP": "?", "LOWER": {"IN": months}}, {"OP": "?", "IS_DIGIT": True},{"OP": "?", "IS_PUNCT": True},{"OP": "?", "IS_DIGIT": True}],
]

matcher.add("LOCATION_AND_DATE_PATTERN", date_patterns)

def parse_query(query):
    date_string = extract_date_string(query)
    dates = None
    if date_string:
        dates = utilities.extract_date_string(date_string)
    else:
        dates = utilities.get_suggested_dates(datetime.now())

    location_list = query.split(date_string)
    location_list.sort(key = len, reverse = True)
    location_list = re.split(r'(-|to)', location_list[0])

    if len(location_list) == 1:
        location = location_list[0]
        return (location,dates)
    else:
        location = location_list[0]
        return (location,dates)


def extract_date_string(query):
    doc = nlp(query)
    matches = matcher(doc)
    match_list =[]
    if matches:
        for match_id, start, end in matches:
            match_list.append(doc[start:end].text)
        match_list.sort(key = len, reverse = True)
        return match_list[0]
    return None

def get_location_from_database(location):
    conn = sqlite3.connect('travel_data.db')
    cur = conn.cursor()
    cur.execute("SELECT id,city FROM us_metro_areas")
    rows = cur.fetchall()

    matches = []

    for row in rows:
        #Write a regex that matches the city
        if row[1] in location:
            matches.append(("us_metro_areas",row[0],row[1]))

    cur.execute("SELECT id,location FROM us_destinations")
    rows = cur.fetchall()

    for row in rows:
        row_tokens = row[1].split()
        
