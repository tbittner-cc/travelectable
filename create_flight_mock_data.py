import replicate

def get_flight_query(src_airport,dest_airport):
    return f"""
    For the airports {src_airport} and {dest_airport} generate 16 flight plans:

    8 for {src_airport} to {dest_airport}
    8 for {dest_airport} to {src_airport}

    Structure the output as:
    Origin | Destination | Airline | (Number of stops (and layover airport(s)))|Departure Time| Arrival Time| Total price in USD

    Use 24-hour time for departure and arrival.

    You do not need to provide city names, only airport codes. 

    USD must include two decimal places (e.g. 250.00, not 250) 

    Do NOT provide any preamble, summary, or disclaimer or any statements like "Here are the 16 flight plans".  
    Only provide the information requested in the format specified.  The information does not need to be accurate but 
    needs to appear accurate.
    """

def execute_llm_query(query,max_tokens = 1024,model='70'):
    data = replicate.run(
        f"meta/meta-llama-3-{model}b-instruct",
         input={"prompt": query, "max_tokens": max_tokens})

    return "".join(data)

with open ('airports.txt', 'r') as f:
    source_data = f.readlines()

with open('query_results.txt', 'a') as f:
    # Data is of this format New York|(JFK, LGA, EWR)\n
    for i_idx,i in enumerate(source_data):
        if i_idx < 6:
            continue
        if i_idx == 7:
            break
        airport_str = i.strip().split('|')[1]
        src_airport_list = [x.strip() for x in airport_str.strip('(').strip(')').split(',')]
        for src_airport in src_airport_list:
            for j_idx,j in enumerate(source_data[i_idx+1:]):
                dest_airport_str = j.strip().split('|')[1]
                dest_airport_list = [x.strip() for x in dest_airport_str.strip('(').strip(')').split(',')]
                for dest_airport in dest_airport_list:
                    print (f"Querying {src_airport} to {dest_airport}")
                    query_results = execute_llm_query(get_flight_query(src_airport,dest_airport))
                    f.write(query_results)
                    f.write('\n')
