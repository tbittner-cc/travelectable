import sqlite3

# Connect to the database
conn = sqlite3.connect('travelectable.db')
cursor = conn.cursor()

# Read the locations file
with open('locations.txt', 'r') as f:
    for line in f:
        location, airport_codes = line.strip().split('(')
        location = location.strip()
        airport_codes = '(' + airport_codes.strip('')

        # Insert the data into the destinations table
        cursor.execute("UPDATE destinations SET airports = ? WHERE location = ?", (airport_codes, location))
        
# Commit the changes and close the connection
conn.commit()
conn.close()