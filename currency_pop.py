import json
import sqlite3

with open('all_locations.txt') as f:
    content = f.readlines()
    content = [x.split('|') for x in content] 

with open('exchange_rates.json') as json_file:
    data = json.load(json_file)
    rates = data['rates']

with sqlite3.connect('travelectable.db') as conn:
    curr = conn.cursor()
    for location in content:
        curr.execute("UPDATE destinations SET currency_code = ?, conversion_rate = ? WHERE location = ?", (location[2].strip(), rates[location[2].strip()], location[0].strip()))
    conn.commit()
