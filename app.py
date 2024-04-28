import os

from amadeus import Client, ResponseError
from flask import Flask,request,redirect, session
from flask import render_template
import spacy

from main import utilities

app = Flask(__name__)
app.secret_key = "super secret key"

# Create an Amadeus client
amadeus = Client(
    client_id=os.environ.get("AMADEUS_API_KEY"),
    client_secret=os.environ.get("AMADEUS_API_SECRET")
)

nlp = spacy.load("en_core_web_sm")

@app.route("/")
def homepage():
    return render_template('homepage.html')

@app.route("/hotels")
def hotels():
    # Get the iataCode for the city
    city_response = amadeus.reference_data.locations.cities.get(keyword=session['hotel_location'])
    iataCode = city_response.data[0]['iataCode']

    hotel_list = amadeus.reference_data.locations.hotels.by_city.get(cityCode=iataCode,radius=15,radiusUnit="MILE")
    hotel_list = sorted(hotel_list.data, key=lambda x: x['distance']['value'])

    hotel_ids = [i['hotelId'] for i in hotel_list]
    
    # Take at most the first 40 hotels
    hotel_ids = hotel_ids[:min(40, len(hotel_ids))]

    hotel_offers = []    
    (start_date,end_date) = session['dates']
    kwargs = {
        'hotelIds': hotel_ids,
        'checkInDate': start_date,
        'checkOutDate': end_date,
        'adults': 2
    }

    search_hotel_response = amadeus.shopping.hotel_offers_search.get(**kwargs)
    print("Hotel offers",len(search_hotel_response.data))
    print("First hotel offer",search_hotel_response.data[0])
    print("First offer",search_hotel_response.data[0]['offers'][0]) 

    # Get the first offer for each hotel that has an offer in our hotelId list
    # Zip the hotelId with the offer to get a list of tuples
    hotel_offers = [i['offers'][0] for i in search_hotel_response.data if i['hotel']['hotelId'] in hotel_ids]

    #for i in search_hotel_response.data:
    #    hotel_offers.append(i)

    return render_template('hotel_search_results.html',hotel_location = session['hotel_location'])

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

    #If no dates are found, return error
    if not date_string:
        error = "No dates provided in query '%s'" % query
        return render_template('homepage.html', error=error)

    dates = utilities.parse_dates(date_string)

    #If no location is found, return error
    if len(locations) == 0:
        #return "Error: No location found"   
        pass
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
