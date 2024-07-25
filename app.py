from datetime import datetime
from flask import Flask,request,redirect, render_template,session
import spacy
import utilities

app = Flask(__name__)
app.secret_key = "super secret key"

nlp = spacy.load("en_core_web_sm")

locations = utilities.get_all_locations()

@app.route("/")
def homepage():
    session.clear
    return render_template('homepage.html',
                           locations = [f"{location[1]}, {location[2]}" for location in locations],
                           suggested_date_range = utilities.get_suggested_dates(datetime.now()))

def add_lead_rates(hotels,dates):
    lead_rates = utilities.get_lead_rates(hotels,session['dates'][0])
    for (hotel_id,rate) in lead_rates:
        for hotel in hotels:
            if hotel['id'] == hotel_id:
                hotel['lead_rate'] = rate

@app.route("/hotels")
def hotels():
    hotels = utilities.get_hotels(session['destination'])
    add_lead_rates(hotels,session['dates'])
    
    return render_template('hotel_search_results.html',hotel_location = session['destination'][1],
                           hotels = hotels,start_date = session['dates'][0],end_date = session['dates'][1],
                           amenities = utilities.get_amenities(session['destination'][0]))

@app.route("/hotel-sort", methods=['GET','POST'])
def hotel_sort():
    hotels = utilities.get_hotels(session['destination'])
    add_lead_rates(hotels,session['dates'])

    sort_option = request.form['sort-hotels-by']
    if sort_option == '':
        pass
    if sort_option == 'price-low':
        hotels = sorted(hotels, key=lambda x: x['lead_rate'])
    elif sort_option == 'price-high':
        hotels = sorted(hotels, key=lambda x: x['lead_rate'], reverse=True)
    elif sort_option == 'rating-high':
        hotels = sorted(hotels, key=lambda x: x['star_rating'], reverse=True)

    template =render_template('hotel_search_card.html',
                        hotel_location = session['destination'][1],
                        hotels = hotels,start_date = session['dates'][0],end_date = session['dates'][1])
    return template

@app.route("/hotel-details", methods=['GET','POST'])
def hotel_details():
    hotel_id = request.form['hotel_id']
    is_winter_rate = utilities.is_winter_rate(session['dates'][0])
    hotel = utilities.get_hotel_details(session['destination'],session['dates'],hotel_id, is_winter_rate)
    return render_template('hotel_details.html',hotel_location = session['destination'],
                           hotel = hotel)

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

    selected_locations = utilities.get_selected_locations(location_queries,locations)

    if location_queries['origin'] == '' and location_queries['destination'] == '':
        error = "No locations found"
        return render_template('homepage.html', locations = [location[1] for location in locations],
                           suggested_date_range = utilities.get_suggested_dates(datetime.now()),
                           error=error)
    # If either origin or destination is empty take the other
    elif location_queries['origin'] == '':
        session['destination'] = selected_locations[1]
        return redirect("/hotels")
    elif location_queries['destination'] == '':
        session['destination'] = selected_locations[0]
        return redirect("/hotels")
    else:
        session['origin'] = selected_locations[0]
        session['destination'] = selected_locations[1]
        return redirect("/hotels")
    return "nlp"
