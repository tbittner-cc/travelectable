import itertools,json,re,sys
sys.path.append('../')
from geopy.distance import geodesic

import utilities

with open("intl_dests_src.txt", "r") as file:
    intl_dests_src = file.read().splitlines()

# Remove duplicates from the list
intl_dests_src = list(set(intl_dests_src))

def custom_sort(x):
    parts = x.split(",")
    if len(parts) > 1:
        return parts[1]
    return x 

intl_dests_src = sorted(intl_dests_src, key=custom_sort)

with open('intl_dests_src_processed.txt', 'w') as output_file:
    output_file.write('\n'.join(intl_dests_src))
