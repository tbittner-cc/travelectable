from datetime import datetime, timedelta
import os

from flask import Flask,request,redirect, session
from flask import render_template
import spacy

import utilities

app = Flask(__name__)
app.secret_key = "super secret key"


nlp = spacy.load("en_core_web_sm")

@app.route("/")
def homepage():
    current_date = datetime.now()
    return render_template('homepage.html',
                           suggested_date_range = utilities.get_suggested_dates(current_date))

@app.route("/hotels")
def hotels():
    session['hotel_offers'] = utilities.get_hotel_offers()
    
    return render_template('hotel_search_results.html',hotel_location = session['hotel_location'],
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
                        hotel_location = session['hotel_location'],
                        hotel_offers = session['hotel_offers'])
    print(template)
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
    # Get the input text from the form
    query = request.form['query']

    doc = nlp(query)
    
    locations = []
    date_string = None
    error = None
    
    for ent in doc.ents:
        if ent.label_ == "GPE": 
            locations.append(ent.text)
        elif ent.label_ == "DATE":
            date_string = ent.text

    if not date_string:
        date_string = utilities.get_suggested_dates(datetime.now())

    dates = utilities.parse_dates(date_string)

    #If no location is found, return error
    if len(locations) == 0:
        error = "No locations provided in query '%s'" % query
        return render_template('homepage.html', error=error)
    #If location contains only one value, go to hotels page
    elif len(locations) == 1:
        session['hotel_location'] = locations[0]
        session['dates'] = dates
        return redirect("/hotels")
    #If location contains more than one value, go to flights page
    elif len(locations) > 1:
        #return redirect("/flights?location=" + "+".join(location))
        pass
    
    print("Location:", locations)
    print("Dates:", dates)

    return "nlp"
