from datetime import datetime
from flask import Flask, make_response, request, redirect, render_template, session
import flight_utilities
import itertools
import os
import utilities
import random

app = Flask(__name__)
app.secret_key = os.environ.get("TRAVELECTABLE_FLASK_SECRET")

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
        "hotel_search_cards.html",
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
        "hotel_search_cards.html",
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
    rate_id = request.form.get("rate_id")
    hotel_id = request.form.get("hotel_id")

    if rate_id and hotel_id:
        is_winter_rate = utilities.is_winter_rate(session["dates"][0])

        hotel = utilities.get_hotel_checkout_details(
            rate_id, session["dates"], is_winter_rate
        )

        return render_template("checkout.html", hotel=hotel)
    else:
        origin_flight = flight_utilities.get_flight_details(
        session["origin_id"], session["dates"][0]
        )
        return_flight = flight_utilities.get_flight_details(
        session["return_id"], session["dates"][1]
         )
        return render_template("checkout.html", origin_flight=origin_flight, return_flight=return_flight,
        flight_pairs=session["flight_pairs"], seat_selections=session["seat_selections"])


@app.route("/complete-booking", methods=["GET", "POST"])
def complete_booking():
    action = request.form["action"]
    print(request.form)
    is_hotel = request.form["is_hotel"]

    if action == "book":
        session.clear()
        return render_template("finished.html")
    elif action == "cancel" and is_hotel != '':
        return redirect("/hotels")
    else:
        return redirect("/origin-flight")


@app.route("/origin-flight")
def origin_flight():
    session["origin_id"] = None
    return _flight(session["origin"], session["destination"], session["dates"][0])

@app.route("/return-flight", methods=["GET", "POST"])
def return_flight():
    return _flight(session["destination"], session["origin"], session["dates"][1])

def _flight(start_location, end_location, flight_date):
    session["return_id"] = None
    session["flight_pairs"] = None
    session["seat_selections"] = None
    session['trip'] = None
    session['leg'] = None

    flights = flight_utilities.get_all_flight_search_results(
        start_location, end_location, flight_date
    )
    flight_filters = flight_utilities.generate_filters(flights)

    if request.form.get("flight_id"):
        origin_flight = flight_utilities.get_flight_details(
            request.form.get("flight_id"), flight_date
        )
    else:
        origin_flight = None

    return render_template(
        "flight_search_results.html",
        start_location=start_location[1],
        end_location=end_location[1],
        start_date=session["dates"][0],
        end_date=session["dates"][1],
        flight_combos=flights,
        flight_filters=flight_filters,
        origin_flight=origin_flight,
    )


@app.route("/flight-amenity-results", methods=["GET", "POST"])
def flight_amenity_results():
    if request.form.get("flight_id"):
        start_location = session["destination"]
        end_location = session["origin"]
        flight_date = session["dates"][1]
        origin_flight = flight_utilities.get_flight_details(
            request.form.get("flight_id"), session["dates"][0]
        )
    else:
        start_location = session["origin"]
        end_location = session["destination"]
        flight_date = session["dates"][0]
        origin_flight = None

    flights = flight_utilities.get_all_flight_search_results(
        start_location, end_location, flight_date
    )

    flight_filters = request.form
    modified_flights = flight_utilities.filter_flights(flight_filters, flights)

    return render_template(
        "flight_search_cards.html",
        start_location=start_location[1],
        end_location=end_location[1],
        start_date=session["dates"][0],
        end_date=session["dates"][1],
        flight_combos=modified_flights,
        origin_flight=origin_flight,
    )


@app.route("/flight-details", methods=["GET", "POST"])
def flight_details():
    if session.get("origin_id") == None:
        session["origin_id"] = request.form["origin_id"]
    if session.get("return_id") == None:
        session["return_id"] = request.form["return_id"]
    if session.get("trip") == None:
        session['trip'] = 0
    if session.get('leg') == None:
        session['leg'] = 0

    origin_flight = flight_utilities.get_flight_details(
        session["origin_id"], session["dates"][0]
    )
    return_flight = flight_utilities.get_flight_details(
        session["return_id"], session["dates"][1]
    )
    trip = session['trip']
    leg = session['leg']

    if session.get("flight_pairs") == None:
        flight_pairs = [(a, b) for a, b in itertools.pairwise(origin_flight["flight_pairs"])]
        airplanes = [flight_utilities.get_flight_seat_configuration(dist) for dist in origin_flight["distances"]]
        origin_flight_pairs = list(zip(flight_pairs,airplanes))

        flight_pairs = [(a, b) for a, b in itertools.pairwise(return_flight["flight_pairs"])]
        airplanes = [flight_utilities.get_flight_seat_configuration(dist) for dist in return_flight["distances"]]
        return_flight_pairs = list(zip(flight_pairs, airplanes))

        session["flight_pairs"] = [origin_flight_pairs, return_flight_pairs]

    flight_pairs = session["flight_pairs"]

    if session.get("seat_selections") == None:
        origin_selections = ['0' for a,b in itertools.pairwise(origin_flight["flight_pairs"])]
        return_selections = ['0' for a,b in itertools.pairwise(return_flight["flight_pairs"])]
        session["seat_selections"] = [origin_selections, return_selections]

    seat_selections = session["seat_selections"]

    trip = session['trip']
    leg = session['leg']

    seat = request.args.get("seat")
    flight = request.args.get("flight")

    if seat != None:
        seat_selections[trip][leg] = seat
        session["seat_selections"] = seat_selections

    if flight == "next":
        if leg + 1 == len(flight_pairs[trip]):
            leg = 0
            trip += 1
        else:
            leg += 1
        if trip == len(flight_pairs):
            return redirect("/checkout")

    if flight == "prev":
        if leg == 0:
            trip -= 1
            leg = len(flight_pairs[trip]) - 1
        else:
            leg -= 1
        if trip == -1:
            return redirect("/origin-flight")

    session['trip'] = trip
    session['leg'] = leg

    unavailable_seat_pct = random.randint(20, 80)

    # First class seats are always unavailable in our simulation, so they
    # aren't eligible to be randomized for availability
    economy_seats = flight_pairs[trip][leg][1]["seat_configuration"]["economy_class"]

    # The nesting for the seats is two deep, hence the double call to itertools.chain
    merged_list = list(itertools.chain(*economy_seats))
    random_eligible_seats = list(itertools.chain(*merged_list))

    unavailable_seats = sorted(
        random.sample(
            random_eligible_seats,
            int(len(random_eligible_seats) * unavailable_seat_pct / 100),
        )
    )

    return render_template(
        "seatmap.html",
        origin_flight=origin_flight,
        return_flight=return_flight,
        unavailable_seats=unavailable_seats,
        seat_selections=seat_selections,
        flight_pairs=flight_pairs,
        trip = session["trip"],
        leg = session["leg"],
    )
