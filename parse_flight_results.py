import sqlite3


with open('flight_results/chicago.txt', 'r') as f:
    source_data = f.readlines()
    # Remove all lines that don't contain a '|'
    source_data = [i for i in source_data if '|' in i]

    with sqlite3.connect("travelectable.db") as conn:
        for idx,entry in enumerate(source_data):
            origin,destination,airline,stops,dep_time,arr_time,price = entry.split('|')
            
            origin = origin.strip()
            destination = destination.strip()
            airline = airline.strip()
            stops = stops.strip()
            dep_time = dep_time.strip()
            arr_time = arr_time.strip()
            price = price.strip()

            if stops.lower() == 'non-stop' or stops.lower() == '0':
                num_stops = 0
                layover_airports = ''
            else:
                stop_tokens = stops.split()
                num_stops = int(stop_tokens[0])
                # Stops are of the following format:
                #| Non-stop |
                #| 1 stop (LAX) |
                #| 2 stops (LAX, ORD) |
                #| 0 |
                #| 1 (LAX) |
                #| 2 (LAX, ORD) |
                if stop_tokens[1].strip()[0] == '(':
                    layover_airports = "".join(stop_tokens[1:])
                else:
                    layover_airports = "".join(stop_tokens[2:])

                curr = conn.cursor()
                curr.execute(
                    """INSERT INTO flight_schedules (origin, destination, airline, num_stops, layover_airports, 
                    departure_time, arrival_time, price) VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
                    (origin, destination, airline, num_stops, layover_airports, dep_time, arr_time, price))
                conn.commit()

        

