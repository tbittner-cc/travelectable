import sqlite3

with sqlite3.connect("travelectable.db") as conn:
    curr = conn.cursor()
    curr.execute("SELECT rr.summer_rate,h.name,d.country FROM room_rates rr join hotels h on rr.hotel_id = h.id join destinations d on h.location_id = d.id where d.country !='USA'")
    rows = curr.fetchall()
    columns = [column[0] for column in curr.description]
    rates = [dict(zip(columns, row)) for row in rows]

    rates.sort(key=lambda x: x['country'])

rate_dict = {}
for rate in rates:
    if rate_dict.get(rate['name']):
        rate_dict[rate['name']][1].append(rate['summer_rate'])
    else:
        rate_dict[rate['name']] = (rate['country'], [rate['summer_rate']])

exchange_rates = 0
for rate in rate_dict.keys():
    country, rates = rate_dict[rate]
    plus_grand_rates = 0
    for num in rates:
        if num >= 1000:
            plus_grand_rates += 1

    if plus_grand_rates >= 2:
        print (rate,rate_dict[rate])

#print(exchange_rates)


