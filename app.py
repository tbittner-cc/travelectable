from datetime import datetime

from flask import Flask,request,redirect, session
from flask import render_template
import spacy

import mock_data,utilities

app = Flask(__name__)
app.config['GENERATE_MOCK_DATA'] = True
app.secret_key = "super secret key"

nlp = spacy.load("en_core_web_sm")

locations = utilities.get_all_locations()

@app.route("/")
def homepage():
    current_date = datetime.now()
    return render_template('homepage.html',
                           locations = [location[1] for location in locations],
                           suggested_date_range = utilities.get_suggested_dates(current_date))

@app.route("/hotels")
def hotels():
    if app.config['GENERATE_MOCK_DATA']:
        mock_data.populate_hotels(session['destination'])
    
    hotels = utilities.get_hotels(session['destination'])
    session['hotels'] = hotels

    lead_rates = utilities.get_lead_rates(hotels,session['dates'][0])
    for (hotel_id,rate) in lead_rates:
        for hotel in hotels:
            if hotel['id'] == hotel_id:
                hotel['lead_rate'] = rate
    
    return render_template('hotel_search_results.html',hotel_location = session['destination'][1],
                           hotels = session['hotels'])

@app.route("/hotel-sort", methods=['GET','POST'])
def hotel_sort():
    sort_option = request.form['sort-hotels-by']
    if sort_option == '':
        session['hotel_offers'] = session['hotel_offers']
    if sort_option == 'price-low':
        session['hotel_offers'] = sorted(session['hotel_offers'], key=lambda x: x['offer_rate'])
    elif sort_option == 'price-high':
        session['hotel_offers'] = sorted(session['hotel_offers'], key=lambda x: x['offer_rate'], reverse=True)
    elif sort_option == 'rating-high':
        session['hotel_offers'] = sorted(session['hotel_offers'], key=lambda x: x['star_rating'], reverse=True)

    template =render_template('hotel_search_results_htmx.html',
                        hotel_location = session['destination'][1],
                        hotel_offers = session['hotel_offers'])
    return template

@app.route("/hotel-details")
def hotel_details():
    session['hotel_details'] = utilities.get_hotel_details()
    if app.config['GENERATE_MOCK_DATA']:
        top_hotels = hotels[:10]
        for hotel in top_hotels:
            mock_data.populate_room_rates(hotel[0],session['destination'])
    is_winter_rate = utilities.is_winter_rate(session['dates'][0])
    for detail in session['hotel_details']:
        detail['is_winter_rate'] = is_winter_rate
    return render_template('hotel_details.html',hotel_location = session['hotel_location'][0],
                           hotel_details = session['hotel_details'])

@app.route("/search", methods=['GET','POST'])
def search():
    location_queries = {'origin': request.form['origin'], 'destination': request.form['destination']}
    date_range = request.form['date_range']

    doc = nlp(date_range)
    
    date_string = None
    error = None
    
    for ent in doc.ents:
        if ent.label_ == "DATE":
            date_string = ent.text

    if not date_string:
        date_string = utilities.get_suggested_dates(datetime.now())

    dates = utilities.parse_dates(date_string)
    session['dates'] = dates

    # If both origin and destination are empty
    if location_queries['origin'] == '' and location_queries['destination'] == '':
        error = "No locations found"
        return render_template('homepage.html', error=error)
    # If either origin or destination is empty take the other
    elif location_queries['origin'] == '':
        session['destination'] = [location for location in locations if location[1] == location_queries['destination']][0]
        if app.config['GENERATE_MOCK_DATA']:
            mock_data.populate_location_description_and_points_of_interest(session['destination'][0],
                                                                           session['destination'][1])
        return redirect("/hotels")
    elif location_queries['destination'] == '':
        session['destination'] = [location for location in locations if location[1] == location_queries['origin']][0]
        if app.config['GENERATE_MOCK_DATA']:
            mock_data.populate_location_description_and_points_of_interest(session['destination'][0],
                                                                           session['destination'][1])
        return redirect("/hotels")
    else:
        session['origin'] = [location for location in locations if location[1] == location_queries['origin']][0]
        session['destination'] = [location for location in locations if location[1] == location_queries['destination']][0]
        if app.config['GENERATE_MOCK_DATA']:
            mock_data.populate_location_description_and_points_of_interest(session['origin'][0],
                                                                           session['origin'][1])
            mock_data.populate_location_description_and_points_of_interest(session['destination'][0],
                                                                           session['destination'][1])
        return redirect("/hotels")
    return "nlp"

