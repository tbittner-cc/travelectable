# The amadeus API has a limit of 3 ratings per call, so we need to break up 
# the list into sublists of 3
def create_hotel_ratings_sublists(hotel_ids):
    offer_id_sub_lists = []
    temp_list = []
    for idx,hotel_id in enumerate(hotel_ids):
        temp_list.append(hotel_id)
        if (idx+1) % 3 == 0:
            offer_id_sub_lists.append(temp_list)
            temp_list = []

    if len(temp_list) > 0:
        offer_id_sub_lists.append(temp_list)

    return offer_id_sub_lists
