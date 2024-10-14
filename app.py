from datetime import datetime
from flask import Flask, make_response, request, redirect, render_template, session
import flight_utilities
import os
import spacy
import utilities

app = Flask(__name__)
app.secret_key = os.environ.get("TRAVELECTABLE_FLASK_SECRET")

nlp = spacy.load("en_core_web_sm")

locations = utilities.get_all_locations()
formatted_locations = [
    f"{location[1]}, {location[2]} {location[3]}" for location in locations
]


@app.route("/")
def homepage():
    session.clear()
    return render_template(
        "homepage.html",
        locations=formatted_locations,
        suggested_date_range=utilities.get_suggested_dates(datetime.now()),
    )


def add_lead_rates(hotels, dates):
    lead_rates = utilities.get_lead_rates(hotels, session["dates"][0])
    for hotel_id, rate in lead_rates:
        for hotel in hotels:
            if hotel["id"] == hotel_id:
                hotel["lead_rate"] = rate


@app.route("/hotels")
def hotels():
    session["filtered_amenities"] = []
    hotels = utilities.get_hotels(session["destination"])
    add_lead_rates(hotels, session["dates"])

    return render_template(
        "hotel_search_results.html",
        hotel_location=session["destination"][1],
        hotels=hotels,
        start_date=session["dates"][0],
        end_date=session["dates"][1],
        amenities=utilities.get_amenities(session["destination"][0]),
    )


@app.route("/hotel-sort", methods=["GET", "POST"])
def hotel_sort():
    hotels = utilities.get_hotels_with_amenities(
        session["destination"], session["filtered_amenities"]
    )
    add_lead_rates(hotels, session["dates"])

    sort_option = request.form["sort-hotels-by"]
    if sort_option == "":
        pass
    if sort_option == "price-low":
        hotels = sorted(hotels, key=lambda x: x["lead_rate"])
    elif sort_option == "price-high":
        hotels = sorted(hotels, key=lambda x: x["lead_rate"], reverse=True)
    elif sort_option == "rating-high":
        hotels = sorted(hotels, key=lambda x: x["star_rating"], reverse=True)

    template = render_template(
        "hotel_search_card.html",
        hotel_location=session["destination"][1],
        hotels=hotels,
        start_date=session["dates"][0],
        end_date=session["dates"][1],
    )
    return template


@app.route("/add-amenity", methods=["GET", "POST"])
def add_amenity():
    all_utilities = utilities.get_amenities(session["destination"][0])
    fa = session["filtered_amenities"]
    # Don't add blanks or incomplete values like "W" for "Wifi"
    if (
        request.form["amenities_input"] != ""
        and request.form["amenities_input"] in all_utilities
    ):
        fa.append(request.form["amenities_input"])
        session["filtered_amenities"] = fa
    resp = make_response(
        render_template(
            "filtered_amenities.html",
            filtered_amenities=session["filtered_amenities"],
            amenities=all_utilities,
        )
    )
    resp.headers.set("HX-Trigger", "updateFilteredAmenities")

    return resp


@app.route("/remove-amenity", methods=["GET", "POST"])
def remove_amenity():
    fa = session["filtered_amenities"]
    # We know we'll only have one key in the form and that maps to our unique amenity value
    value = list(request.form.to_dict().values())[0]
    fa.remove(value)
    session["filtered_amenities"] = fa
    resp = make_response(
        render_template(
            "filtered_amenities.html",
            filtered_amenities=session["filtered_amenities"],
            amenities=utilities.get_amenities(session["destination"][0]),
        )
    )
    resp.headers.set("HX-Trigger", "updateFilteredAmenities")

    return resp


@app.route("/hotel-amenity-results", methods=["GET", "POST"])
def hotel_amenity_results():
    hotels = utilities.get_hotels_with_amenities(
        session["destination"], session["filtered_amenities"]
    )
    add_lead_rates(hotels, session["dates"])

    template = render_template(
        "hotel_search_card.html",
        hotel_location=session["destination"][1],
        hotels=hotels,
        start_date=session["dates"][0],
        end_date=session["dates"][1],
    )
    return template


@app.route("/hotel-details", methods=["GET", "POST"])
def hotel_details():
    hotel_id = request.form["hotel_id"]
    is_winter_rate = utilities.is_winter_rate(session["dates"][0])
    hotel = utilities.get_hotel_details(
        session["destination"], session["dates"], hotel_id, is_winter_rate
    )
    return render_template(
        "hotel_details.html", hotel_location=session["destination"], hotel=hotel
    )


@app.route("/search", methods=["GET", "POST"])
def search():
    location_queries = {
        "origin": request.form["origin"],
        "destination": request.form["destination"],
    }

    date_range = {"from": request.form["from"], "to": request.form["to"]}

    # Check if both date_range values are empty
    if date_range["from"] == "" and date_range["to"] == "":
        dates = utilities.get_suggested_dates(datetime.now())
    else:
        dates = utilities.parse_dates(date_range["from"], date_range["to"])
    session["dates"] = dates

    selected_locations = utilities.get_selected_locations(location_queries, locations)

    if location_queries["origin"] == "" and location_queries["destination"] == "":
        error = "No locations found"
        return render_template(
            "homepage.html",
            locations=[location[1] for location in locations],
            suggested_date_range=utilities.get_suggested_dates(datetime.now()),
            error=error,
        )
    # If either origin or destination is empty take the other and redirect to hotels
    elif location_queries["origin"] == "":
        session["destination"] = selected_locations[1]
        return redirect("/hotels")
    elif location_queries["destination"] == "":
        session["destination"] = selected_locations[0]
        return redirect("/hotels")
    else:
        session["origin"] = selected_locations[0]
        session["destination"] = selected_locations[1]
        return redirect("/origin-flight")


@app.route("/filter-origins", methods=["GET", "POST"])
def filter_origins():
    return _filter_locations(request.form["origin"])


@app.route("/filter-destinations", methods=["GET", "POST"])
def filter_destinations():
    return _filter_locations(request.form["destination"])


def _filter_locations(form_value):
    substring = form_value.lower()
    filtered_locations = [
        location for location in formatted_locations if substring in location.lower()
    ]
    return render_template("location_options.html", locations=filtered_locations)


@app.route("/checkout", methods=["GET", "POST"])
def checkout():
    rate_id = request.form["rate_id"]
    hotel_id = request.form["hotel_id"]

    is_winter_rate = utilities.is_winter_rate(session["dates"][0])

    hotel = utilities.get_hotel_checkout_details(
        rate_id, session["dates"], is_winter_rate
    )
    return render_template("checkout.html", hotel=hotel)


@app.route("/complete-booking", methods=["GET", "POST"])
def complete_booking():
    action = request.form["action"]

    if action == "book":
        return render_template("finished.html")
    elif action == "cancel":
        return redirect("/hotels")


@app.route("/origin-flight")
def flight():
    origins = flight_utilities.retrieve_airports(session["origin"])
    destinations = flight_utilities.retrieve_airports(session["destination"])

    origin_flights = flight_utilities.get_all_flight_search_results(session["origin"], session['destination'], session["dates"][0])

    flight_combos = origin_flights
    flight_filters = flight_utilities.generate_filters(origin_flights)

    return render_template(
        "flight_search_results.html",
        origin_location=session["origin"][1],
        destination_location=session["destination"][1],
        start_date=session["dates"][0],
        end_date=session["dates"][1],
        flight_combos=flight_combos,
        flight_filters=flight_filters,
    )

@app.route("/return-flight",methods=["GET", "POST"])
def return_flight():
    origin_flight = request.form["flight_id"]
    return origin_flight

@app.route("/flight-amenity-results", methods=["GET", "POST"])
def flight_amenity_results():
    return request.form