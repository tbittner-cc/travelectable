import itertools,re,sys
sys.path.append('../')

import utilities

test_data = """
Here are the largest cities in each metropolitan area:
[(New York|NY|USA), (Los Angeles|CA|USA), 
(Chicago|IL|USA), (Houston|TX|USA), 
(Phoenix|AZ|USA), (Philadelphia|PA|USA), 
(San Antonio|TX|USA), (San Diego|CA|USA), 
(Dallas|TX|USA), (San Jose|CA|USA)]
Let me know if you need anything else!
"""

with open('us_metro_areas.txt', 'r') as file:
    data = file.read()

us_cities = []
for line in data.splitlines():
    parts = line.split(':')
    if len(parts) == 2:
        metro_area = parts[0].strip()
        population = parts[1].strip()
        us_cities.append({'metro_area': metro_area, 'population': population})

cities_sub_list = [us_cities[i:i+10] for i in range(0, len(us_cities), 10)]

cities_new_sub_list = []

location_pattern = r'\((.*?)\|(.*?)\|(.*?)\)'
for city_list in cities_sub_list:
    query = """For the following metro areas return the largest city in the area in the following format:

        [(<city>|<state>|<country>),...]

        {}""".format("\n".join([city['metro_area'] for city in city_list]))
    print(query)

    data = utilities.execute_llm_query(query)
    matches = re.findall(location_pattern, data)
    result = [{'city': match[0], 'state': match[1], 'country': match[2]} for match in matches]

    merged_list = [{**city_list[i], **result[i]} for i in range(len(city_list))]
    cities_new_sub_list.append(merged_list)

us_cities = list(itertools.chain.from_iterable(cities_new_sub_list))

with open('us_cities.txt', 'w') as output_file:
    output_file.write(str(us_cities))
