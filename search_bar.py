import re,sqlite3

import spacy
from spacy.matcher import Matcher

nlp = spacy.load("en_core_web_sm")
matcher = Matcher(nlp.vocab)

months = ["january", "february", "march", "april", 
        "may", "june", "july", "august", 
        "september", "october", "november", "december",
        "jan", "feb", "mar", "apr", 
        "may", "jun", "jul", "aug", 
        "sep", "oct", "nov", "dec"]

# date_patterns = [
#     [{"LOWER": {"IN": months}},{"IS_DIGIT": True}, 
     
#      {"OP": "?", "IS_PUNCT": True}, {"OP": "?", "LOWER": "to"},
     
#      {"OP": "?", "LOWER": {"IN": months}}, {"OP": "?", "IS_DIGIT": True}],
# ]

date_patterns = [
    [{"LOWER": {"IN": months}},{"IS_DIGIT": True}],
]

matcher.add("LOCATION_AND_DATE_PATTERN", date_patterns)

def parse_dates(query):
    doc = nlp(query)
    matches = matcher(doc)
    match_list =[]
    if matches:
        for match_id, start, end in matches:
            match_list.append(doc[start:end].text)
        match_list.sort(key = len, reverse = True)
        return match_list
    return None

def is_location_in_database(location):
    conn = sqlite3.connect('travel_data.db')
    cur = conn.cursor()
    cur.execute("SELECT city FROM us_metro_areas")
    rows = cur.fetchall()

    for row in rows:
        #Write a regex that matches the city
        if re.match(location, row[0]):
            pass



# Process the text
if __name__ == '__main__':
    doc = nlp("may 28 - june 5")
    matches = matcher(doc)
    if matches:
        for match_id, start, end in matches:
            print("Matched: ", doc[start:end])
            print("Span: ", doc[start:end].text)