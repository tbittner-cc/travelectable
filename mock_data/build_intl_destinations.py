import itertools,json,re,sys
sys.path.append('../')

import utilities

test_data = """
Here are the requested information:

(29.9717|31.2538|Exercise Increased Precautions), (-34.6037|-58.3816|Exercise Normal Precautions), 
(45.5017|-73.5673|Exercise Normal Precautions), (48.2082|16.3738|Exercise Normal Precautions), 
(50.0755|14.4378|Exercise Normal Precautions)

Note: The travel advisory levels are subject to change and may not reflect the most up-to-date 
information. For the latest guidance, please check with a travel advisory website.
"""

with open("intl_dests_src.txt", "r") as file:
    intl_dests_src = file.read().splitlines()

# Remove duplicates from the list
intl_dests_src = list(set(intl_dests_src))
intl_dests_src.sort()

intl_loc_list = []

location_pattern = r'\((.*?)\|(.*?)\|(.*?)\)'
for dest in intl_dests_src:
    if ("," in dest):
        parts = dest.split(",")
        dest = {"location": parts[0].strip(), "country": parts[1].strip()}
    else:
        dest = {"location": dest.strip(), "country": dest.strip()}
    intl_loc_list.append(dest)

intl_loc_sublists = utilities.build_sublist(intl_loc_list, 5)

new_intl_loc_sublists = []

for sub_list in intl_loc_sublists:
    loc_list = [f"{loc['location']}, {loc['country']}" for loc in sub_list]
    loc_query_string = "\n".join(loc_list)

    query = """For the following locations return the lat, long, and the state department 
    travel advisory level in the following format with the most up-to-date information 
    you have available. You must provide an answer, even if it's an estimate. Ensure the 
    advisory level is one of "Exercise Normal Precautions" 
    "Exercise Increased Precautions" "Reconsider Travel" or "Do Not Travel".  Do not add
    disclaimers or summaries to the response.

    [(<latitude>|<longitude>|<travel_advisory_level>),...]

    {}""".format(loc_query_string)

    data = utilities.execute_llm_query(query)

    matches = re.findall(location_pattern, data)
    result = [{'latitude': match[0], 'longitude': match[1], 'travel_advisory_level': match[2]} for match in matches]
    merged_list = [{**sub_list[i], **result[i]} for i in range(len(sub_list))]

    new_intl_loc_sublists.append(merged_list)

intl_dests = list(itertools.chain.from_iterable(new_intl_loc_sublists))

with open('intl_dests.txt', 'w') as output_file:
    output_file.write(json.dumps(intl_dests,indent=4))
