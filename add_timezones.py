import sqlite3

with open('timezones.txt', 'r') as f:
    loc_tz_pairs = [(loc.strip(), tz.strip()) for loc, tz in [i.split('|') for i in f.readlines()]]

    with sqlite3.connect("travelectable.db") as conn:
        curr = conn.cursor()
        for loc, tz in loc_tz_pairs:
            curr.execute("""UPDATE destinations SET timezone = ? WHERE location = ?""", (tz, loc, ))
        conn.commit()
