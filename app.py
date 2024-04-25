from flask import Flask,request,redirect
from flask import render_template

import spacy

from main import search

app = Flask(__name__)

nlp = spacy.load("en_core_web_sm")

@app.route("/")
def homepage():
    return render_template('homepage.html')

@app.route("/hotels")
def hotels():
    return render_template('hotel_search_results.html')

@app.route("/search")
def search():
    # Get the input text from the form
    query = request.args.get('query')

    doc = nlp(query)
    
    locations = []
    date_string = None
    
    for ent in doc.ents:
        if ent.label_ == "GPE": 
            locations.append(ent.text)
        elif ent.label_ == "DATE":
            date_string = ent.text

    #If no dates are found, return error
    if not date_string:
        return "Error: No dates found"

    dates = search.parse_dates(date_string)

    #If no location is found, return error
    if len(locations) == 0:
        #return "Error: No location found"   
        pass
    #If location contains only one value, go to hotels page
    elif len(locations) == 1:
        #return redirect("/hotels?location=" + location[0] + "&dates=" + dates)
        return render_template('hotel_search_results.html')
    #If location contains more than one value, go to flights page
    elif len(locations) > 1:
        #return redirect("/flights?location=" + "+".join(location))
        pass
    
    print("Location:", locations)
    print("Dates:", dates)

    return "nlp"
