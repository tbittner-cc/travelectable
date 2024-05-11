import re,sys
sys.path.append('../')

import utilities

from geopy.geocoders import Nominatim

# Sample source data
# {'metro_area': 'New York-Newark-Jersey City, NY-NJ-PA', 'population': '19,620,000', 'city': 'New York', 'state': 'NY', 'country': 'USA'}

# Open us_cities.txt and extract the city, state, and country
with open('us_cities.txt', 'r') as file:
    data = file.read()

# Write a regex pattern to extract the city, state, and country from test_data
location_pattern = r"'city':\s*'(?P<city>[^']+)',\s*'state':\s*'(?P<state>[^']*)',\s*'country':\s*'(?P<country>[^']+)'"

# Use the regex pattern to extract the city, state, and country from us_cities.txt
matches = re.findall(location_pattern, data)

locations = [f"{match[0]}, {match[1]}, {match[2]}" for match in matches]

# Use Nominatim to get the latitude and longitude of each location
#geolocator = Nominatim(user_agent="travelectable")
#geocodes = [geolocator.geocode(location) for location in locations]
#for idx,geocode in enumerate(geocodes):
#    print(locations[idx], geocode.address, geocode.latitude, geocode.longitude)


