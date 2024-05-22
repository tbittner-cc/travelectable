from datetime import datetime
import sqlite3

from flask import Flask,request,redirect, session
from flask import render_template
import spacy

import utilities

app = Flask(__name__)
app.secret_key = "super secret key"

nlp = spacy.load("en_core_web_sm")

locations = []
with sqlite3.connect('travel_data.db') as conn:
    curr = conn.cursor()
    curr.execute("SELECT id,location,city,state,country FROM destinations WHERE country = 'USA'")
    rows = curr.fetchall()
    for row in rows:
        if row[2] != '':
            locations.append((row[0],f"{row[2]}, {row[3]} {row[4]}"))
        else:
            locations.append((row[0],f"{row[1]}, {row[3]} {row[4]}"))

    curr.execute("SELECT id,location,country FROM destinations WHERE country != 'USA'")
    rows = curr.fetchall()
    for row in rows:
        locations.append((row[0],f"{row[1]}, {row[2]}"))

@app.route("/")
def homepage():
    current_date = datetime.now()
    return render_template('homepage.html',
                           locations = [location[1] for location in locations],
                           suggested_date_range = utilities.get_suggested_dates(current_date))

@app.route("/hotels")
def hotels():
    session['hotel_offers'] = utilities.get_hotel_offers()
    
    return render_template('hotel_search_results.html',hotel_location = session['destination'],
                           hotel_offers = session['hotel_offers'])

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
                        hotel_location = session['destination'],
                        hotel_offers = session['hotel_offers'])
    return template

@app.route("/hotel-details")
def hotel_details():
    session['hotel_details'] = utilities.get_hotel_details()
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
        session['destination'] = location_queries['destination']
        return redirect("/hotels")
    elif location_queries['destination'] == '':
        session['destination'] = location_queries['origin']
        return redirect("/hotels")
    else:
        session['origin'] = location_queries['origin']
        session['destination'] = location_queries['destination']

    return "nlp"
