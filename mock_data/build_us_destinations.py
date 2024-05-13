import itertools,json,re,sys
sys.path.append('../')
from geopy.distance import geodesic

import utilities

# Sample query data response from Llama-3
# Here are the locations with their corresponding state abbreviations, latitudes, and longitudes:
#
# [(ME|44.3129|-68.2211), (NC|35.5959|-82.5515), (ME|44.3879|-68.2039), (OR|44.0582|-121.3155), (CA|36.2707|-121.5859)]
#
# Here's a breakdown of each location:
# Acadia National Park, Maine: ME|44.3129|-68.2211
# Asheville, North Carolina: NC|35.5959|-82.5515
# Bar Harbor, Maine: ME|44.3879|-68.2039
# Bend, Oregon: OR|44.0582|-121.3155
# Big Sur, California: CA|36.2707|-121.5859
#
# Let me know if you have any further questions!

with open("us_dests_src.txt", "r") as file:
    us_dests_src = file.read().splitlines()

# Remove duplicates from the list
us_dests_src = list(set(us_dests_src))
us_dests_src.sort()

us_dests_src = [location.split(",") for location in us_dests_src]
us_dests_src = [{"location": location[0].strip(), "state": location[1].strip()} for location in us_dests_src]

with open("us_cities.txt", "r") as file:
    us_cities = json.loads(file.read())

city_names = [f"{city['city']}" for city in us_cities]

# Delete any elements in us_dests_src where location is in city_names
# These are large US cities, so looking by city name is sufficient
us_dests_src = [city for city in us_dests_src if city['location'] not in city_names]

# Build sublists of 5 because we're asking for more information than usual and 
# don't want to stress our precious LLM out.
us_dests_sub_list = utilities.build_sublist(us_dests_src, 5)

new_us_dests_sub_list = []

location_pattern = r'\((.*?)\|(.*?)\|(.*?)\)'
for sub_list in us_dests_sub_list:
    # For each item in the sublist combine the location and state into a single string
    loc_list = [f"{loc['location']}, {loc['state']}" for loc in sub_list]
    loc_query_string = "\n".join(loc_list)

    # Build the query
    query = """For the following locations return the state as a two letter abbreviation 
    and the lat and long in the following format:
    
    [(<state_abbreviation>|<latitude>|<longitude>),...]

    {}""".format(loc_query_string)

    data = utilities.execute_llm_query(query)
    matches = re.findall(location_pattern, data)
    result = [{'state': match[0], 'latitude': match[1], 'longitude': match[2]} for match in matches]
    sub_list = [{'location': sub_list[i]['location'], 'state': result[i]['state'], 
                 'latitude': result[i]['latitude'], 'longitude': result[i]['longitude']} 
                 for i in range(len(sub_list))]

    new_us_dests_sub_list.append(sub_list)

us_dests = list(itertools.chain.from_iterable(new_us_dests_sub_list))

# For every element in us_dests calculate the distance to each element in us_cities
for dest in us_dests:
    distances =[{'metro_area': city['metro_area'], 
      'distance': geodesic((dest['latitude'], dest['longitude']), (city['latitude'], city['longitude'])).miles} 
      for city in us_cities]
    distances.sort(key=lambda x: x['distance'])
    dest['nearest_metro_area'] = distances[0]['metro_area']
    # Add country to us_dests in case we need it later
    dest['country'] = 'USA'

with open('us_dests.txt', 'w') as output_file:
    output_file.write(json.dumps(us_dests,indent=4))
