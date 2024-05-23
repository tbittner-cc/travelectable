import json,sqlite3

import replicate

def execute_llm_query(query,max_tokens = 512):
    data = replicate.run(
        "meta/meta-llama-3-70b-instruct",
         input={"prompt": query, "max_tokens": max_tokens})
    
    return "".join(data)

def get_location_description_query(location):
    return f"""
    Write a 100-word marketing description for visiting {location}.  
    
    Format it as [<description>]

    Do not add a summary or disclaimer at the beginning or end of your reply. Do not deviate from the format.
    """

def get_location_points_of_interest_query(location):
    return f"""
    Provide 5 points of interest for {location}  

    Format it as <point_of_interest>|<point_of_interest>|<point_of_interest>|<point_of_interest>|<point_of_interest>

    Do not add a summary or disclaimer at the beginning or end of your reply. Do not deviate from the format.
    """

def execute_llm_query(query,max_tokens = 512):
    data = replicate.run(
        "meta/meta-llama-3-70b-instruct",
         input={"prompt": query, "max_tokens": max_tokens})
    
    return "".join(data)

def populate_location_description_and_points_of_interest(location_id,location_query,force_flag=False):
    with sqlite3.connect('travel_data.db') as conn:
        curr = conn.cursor()
        curr.execute("SELECT id,description,points_of_interest FROM destinations WHERE id = ?", (location_id,))
        rows = curr.fetchall()
        data = rows[0]

    if data[1] == '' or data[1] == None or force_flag:
        query = get_location_description_query(location_query)
        print(query)
        description = execute_llm_query(query)
        print (description)
        description = description.strip('[').strip(']')
        with sqlite3.connect('travel_data.db') as conn:
            curr = conn.cursor()
            curr.execute("UPDATE destinations SET description = ? WHERE id = ?", (description,location_id))
            conn.commit()

    if data[2] == '' or data[2] == None or force_flag:
        query = get_location_points_of_interest_query(location_query)
        print(query)
        points_of_interest = execute_llm_query(query)
        print (points_of_interest)
        points_of_interest = points_of_interest.split('|')
        with sqlite3.connect('travel_data.db') as conn:
            curr = conn.cursor()
            curr.execute("UPDATE destinations SET points_of_interest = ? WHERE id = ?", (str(points_of_interest),location_id))
            conn.commit()