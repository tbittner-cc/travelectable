import ast
import sqlite3

with sqlite3.connect("travelectable.db") as conn:
    curr = conn.cursor()
    curr.execute("SELECT id,amenities FROM room_rates")
    rows = curr.fetchall()

amenities_set = set()
amenities_xref = {}
for row in rows:
    am_list = ast.literal_eval(row[1])
    for am in am_list:
        amenity = am[0].upper().strip() + am[1:].lower().strip()
        if amenity not in amenities_set:
            amenities_set.add(amenity)
            amenities_xref[amenity] = [row[0]]
        else:
            amenities_xref[amenity].append(row[0])

with sqlite3.connect("travelectable.db") as conn:
    curr = conn.cursor()
    for am, room_rate_ids in amenities_xref.items():
        curr.execute("INSERT INTO amenities (amenity) VALUES (?)", (am,))
        new_id = curr.lastrowid

        for room_rate_id in room_rate_ids:
            curr.execute("INSERT INTO room_rates_amenities_xref (room_rate_id,amenity_id) VALUES (?,?)",
                         (room_rate_id, new_id))
    conn.commit()
    