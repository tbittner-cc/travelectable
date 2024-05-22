import sqlite3

# # Connect to the database (create it if it doesn't exist)
# conn = sqlite3.connect('travel_data.db')

# # Create a cursor object
# cursor = conn.cursor()

# # Create the table
# create_table_query = '''
#     CREATE TABLE IF NOT EXISTS destinations (
#         id INTEGER PRIMARY KEY,
#         location VARCHAR,
#         city VARCHAR,
#         state VARCHAR,
#         country VARCHAR,
#         latitude VARCHAR,
#         longitude VARCHAR,
#         description VARCHAR,
#         points_of_interest VARCHAR,
#         nearest_metro_area VARCHAR,
#         travel_advisory_level VARCHAR(30)
#     )
# '''
# cursor.execute(create_table_query)

# # Commit the changes and close the connection
# conn.commit()
# conn.close()

with sqlite3.connect('travel_data.db') as conn:
    cur = conn.cursor()
    cur.execute("SELECT location,country,latitude,longitude,description,points_of_interest,travel_advisory_level FROM intl_destinations")
    rows = cur.fetchall()
    for row in rows:
        cur.execute("INSERT INTO destinations (location,country,latitude,longitude,description,points_of_interest,travel_advisory_level) VALUES (?,?,?,?,?,?,?)", row)
    conn.commit()
    cur.close()
