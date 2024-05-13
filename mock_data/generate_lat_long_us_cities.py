import itertools,json,re,sys
sys.path.append('../')

import utilities

# Sample source data
# {'metro_area': 'New York-Newark-Jersey City, NY-NJ-PA', 'population': '19,620,000', 'city': 'New York', 'state': 'NY', 'country': 'USA'}

# Sample output data
# Here are the latitude and longitude coordinates for each location:
# [(34.0522|-118.2437), (40.7128|-74.0060), (41.8781|-87.6298), (30.0521|-90.0716), (30.2672|-97.7431)]
# Let me know if you need anything else!

with open('us_cities.txt', 'r') as file:
    data = file.read()
us_cities = json.loads(data)

sub_locations = utilities.build_sublist(us_cities, 10)

new_sub_locations = []

location_pattern = r'\(\s*(.*?)\s*\|\s*(.*?)\s*\)'
for sub_loc_list in sub_locations:
    city_list = "\n".join([f"{city['city']}, {city['state']}, {city['country']}" for city in sub_loc_list])

    query = """For the following locations provide latitude and longitude in the following format:

    [(<latitude>|<longitude>),...]

    {}
    """.format(city_list)

    data = utilities.execute_llm_query(query)
    matches = re.findall(location_pattern, data)
    result = [{'latitude': match[0], 'longitude': match[1]} for match in matches]

    merged_list = [{**sub_loc_list[i], **result[i]} for i in range(len(sub_loc_list))]
    new_sub_locations.append(merged_list)

us_cities = list(itertools.chain.from_iterable(new_sub_locations))

with open('us_cities.txt', 'w') as output_file:
    output_file.write(json.dumps(us_cities,indent=4))
