from flask import Flask
from flask import render_template

import spacy

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template('homepage.html')

@app.route("/spacy")
def spacy_test():
    nlp = spacy.load("en_core_web_sm")
    doc = nlp("New York May 7-12")
    
    location = None
    dates = None
    
    for ent in doc.ents:
        if ent.label_ == "GPE":  # GPE stands for Geopolitical Entity, which includes countries, cities, etc.
            location = ent.text
        elif ent.label_ == "DATE":
            dates = ent.text
    
    print("Location:", location)
    print("Dates:", dates)

    return "hello nlp"
