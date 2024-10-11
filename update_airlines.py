import random 
import sqlite3

with sqlite3.connect("travelectable.db") as conn:
    curr = conn.cursor()

    airline_list = ["Aerius Global","Aurora Voyages","Celestial Wings","Horizon Connect","Skypath Airways"]
    curr.execute("SELECT id from flight_schedules")
    rows = curr.fetchall()
    ids = [row[0] for row in rows]

    for id in ids:
        curr.execute("UPDATE flight_schedules SET airline = ? WHERE id = ?", (random.choice(airline_list), id))
    conn.commit()
    