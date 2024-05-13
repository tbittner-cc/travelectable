import json

# Open us_dests_src.txt and read the contents into a list
with open("us_dests_src.txt", "r") as file:
    us_dests_src = file.read().splitlines()

# Remove duplicates from the list
us_dests_src = list(set(us_dests_src))

# Split each element of the list into two parts and assign each part to a dict {'city', 'country'}
us_dests_src = [location.split(",") for location in us_dests_src]
us_dests_src = [{"location": location[0].strip(), "state": location[1].strip()} for location in us_dests_src]

with open("us_cities.txt", "r") as file:
    us_cities = json.loads(file.read())

city_names = [f"{city['city']}" for city in us_cities]

# Delete any elements in us_dests_src where location is in city_names
us_dests_src = [city for city in us_dests_src if city['location'] not in city_names]

# Print the location key of the remaining elements in us_dests_src
for city in us_dests_src:
    print(city['location'])

