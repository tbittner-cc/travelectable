import sqlite3
import ast

with sqlite3.connect("travelectable.db") as conn:
    curr = conn.cursor()
    curr.execute("SELECT amenities FROM room_rates")
    rows = curr.fetchall()

    unique_amenities = set()
    for row in rows:
        row = ast.literal_eval(row[0])
        unique_amenities.update(row)

print(len(unique_amenities))

unique_amenities = sorted(list(unique_amenities))
with open("unique_amenities.txt", "w") as f:
    for amenity in unique_amenities:
        f.write(amenity + "\n")