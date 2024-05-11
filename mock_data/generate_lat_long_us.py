import re,sys
sys.path.append('../')

import utilities

from geopy.geocoders import Nominatim

# Sample source data
# {'metro_area': 'New York-Newark-Jersey City, NY-NJ-PA', 'population': '19,620,000', 'city': 'New York', 'state': 'NY', 'country': 'USA'}

# Sample output data
# Here are the latitude and longitude coordinates for each location:
# [(34.0522|-118.2437), (40.7128|-74.0060), (41.8781|-87.6298), (30.0521|-90.0716), (30.2672|-97.7431), (38.8950|-77.0365)]
# Let me know if you need anything else!

# Open us_cities.txt and extract the city, state, and country
with open('us_cities.txt', 'r') as file:
    data = file.read()

# Write a regex pattern to extract the city, state, and country from test_data
location_pattern = r"'city':\s*'(?P<city>[^']+)',\s*'state':\s*'(?P<state>[^']*)',\s*'country':\s*'(?P<country>[^']+)'"

# Use the regex pattern to extract the city, state, and country from us_cities.txt
matches = re.findall(location_pattern, data)

locations = [f"{match[0]}, {match[1]}, {match[2]}" for match in matches]

sub_locations = utilities.build_sublist(locations, 10)

#Get the index of the last comma in "Austin, TX, USA" and return everything before it

for sub_loc_list in sub_locations:
    city_list = "\n".join(sub_loc_list)
    query = """For the following locations provide latitude and longitude in the following format:

    [(<latitude>,<longitude>),...]

    {}
    """.format(city_list)
    print(query)
    print()

# Use Nominatim to get the latitude and longitude of each location
#geolocator = Nominatim(user_agent="travelectable")
#geocodes = [geolocator.geocode(location) for location in locations]
#for idx,geocode in enumerate(geocodes):
#    print(locations[idx], geocode.address, geocode.latitude, geocode.longitude)


