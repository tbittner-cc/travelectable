from flask import Flask,request,redirect
from flask import render_template

import spacy

from app import search

app = Flask(__name__)

nlp = spacy.load("en_core_web_sm")

@app.route("/")
def homepage():
    return render_template('homepage.html')

@app.route("/search")
def search():
    # Get the input text from the form
    query = request.args.get('query')

    doc = nlp(query)
    
    location = []
    dates = None
    
    for ent in doc.ents:
        if ent.label_ == "GPE": 
            location.append(ent.text)
        elif ent.label_ == "DATE":
            dates = ent.text

    #If no dates are found, return error
    if not dates:
        return "Error: No dates found"

    search.get_dates(dates)

    #If no location is found, return error
    if len(location) == 0:
        #return "Error: No location found"   
        pass
    #If location contains only one value, go to hotels page
    elif len(location) == 1:
        #return redirect("/hotels?location=" + location[0] + "&dates=" + dates)
        pass
    #If location contains more than one value, go to flights page
    elif len(location) > 1:
        #return redirect("/flights?location=" + "+".join(location))
        pass
    
    print("Location:", location)
    print("Dates:", dates)

    return "nlp"
