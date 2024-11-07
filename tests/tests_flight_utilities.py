from datetime import datetime
import unittest
import flight_utilities
import pytz


class TestRetrieveAirports(unittest.TestCase):
    def test_retrieve_airports(self):
        result = flight_utilities.retrieve_airports((8, "Boston", "USA", "(BOS)"))
        self.assertEqual(result, ["BOS"])

        result = flight_utilities.retrieve_airports(
            (1, "New York", "USA", "(JFK, LGA, EWR)")
        )
        self.assertEqual(result, ["JFK", "LGA", "EWR"])


class TestGetFlightDuration(unittest.TestCase):
    def test_get_flight_duration(self):
        flight_date = datetime(2024, 10, 10)
        departure_time = datetime.strptime("06:00", "%H:%M")
        arrival_time = datetime.strptime("08:30", "%H:%M")
        origin_tz = pytz.timezone("US/Central")
        destination_tz = pytz.timezone("US/Eastern")
        result = flight_utilities.get_flight_duration(
            flight_date, departure_time, arrival_time, origin_tz, destination_tz
        )
        self.assertEqual(result, "1h 30m")

        departure_time = datetime.strptime("22:00", "%H:%M")
        arrival_time = datetime.strptime("01:00", "%H:%M")
        result = flight_utilities.get_flight_duration(
            flight_date, departure_time, arrival_time, origin_tz, destination_tz
        )
        self.assertEqual(result, "2h 0m")


class TestGetAllFlightSearchResults(unittest.TestCase):
    def test_get_all_flight_search_results(self):
        result = flight_utilities.get_all_flight_search_results(
            (1, "New York", "USA", "(JFK, LGA, EWR)"),
            (3, "Chicago", "USA", "(ORD,MDW)"),
            datetime(2024, 10, 10),
        )
        self.assertEqual(len(result), 48)

        result = sorted(result, key=lambda x: x["id"])
        first_result = result[0]
        self.assertEqual(first_result["origin"], "JFK")
        self.assertEqual(first_result["destination"], "ORD")
        self.assertEqual(first_result["airline"], "Horizon Connect")
        self.assertEqual(
            first_result["arrival_time"], datetime.strptime("08:30", "%H:%M")
        )
        self.assertEqual(
            first_result["departure_time"], datetime.strptime("06:00", "%H:%M")
        )
        self.assertEqual(first_result["layover_airports"], "")
        self.assertEqual(first_result["num_stops"], 0)


class TestGenerateFilters(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None

    def test_generate_filters(self):
        flight_results = flight_utilities.get_all_flight_search_results(
            (1, "New York", "USA", "(JFK, LGA, EWR)"),
            (3, "Chicago", "USA", "(ORD,MDW)"),
            datetime(2024, 10, 10),
        )

        result = flight_utilities.generate_filters(flight_results)
        self.assertEqual(
            result,
            {
                "stops": {0: 25, 1: 23},
                "airlines": {
                    "Aerius Global": 6,
                    "Aurora Voyages": 10,
                    "Celestial Wings": 15,
                    "Horizon Connect": 11,
                    "Skypath Airways": 6,
                },
                "layover_airports": {
                    "BOS": 1,
                    "BWI": 4,
                    "CLE": 1,
                    "CVG": 1,
                    "DEN": 1,
                    "DTW": 4,
                    "EWR": 3,
                    "JFK": 1,
                    "MDW": 1,
                    "ORD": 3,
                    "PIT": 3,
                },
            },
        )


class TestFilterFlights(unittest.TestCase):
    def test_filter_flights(self):
        flight_results = flight_utilities.get_all_flight_search_results(
            (1, "New York", "USA", "(JFK, LGA, EWR)"),
            (3, "Chicago", "USA", "(ORD,MDW)"),
            datetime(2024, 10, 10),
        )

        flight_filters = {"0-stop": "on"}

        result = flight_utilities.filter_flights(flight_filters, flight_results)
        self.assertEqual(len(result), 25)

        flight_filters = {"0-stop": "on", "1-stop": "on"}

        result = flight_utilities.filter_flights(flight_filters, flight_results)
        self.assertEqual(len(result), 48)

        flight_filters = {"airline-Aerius Global": "on"}

        result = flight_utilities.filter_flights(flight_filters, flight_results)
        self.assertEqual(len(result), 6)

        flight_filters = {"airport-BWI": "on"}

        result = flight_utilities.filter_flights(flight_filters, flight_results)
        self.assertEqual(len(result), 4)

        flight_filters = {"airport-BWI": "on", "airline-Celestial Wings": "on"}

        result = flight_utilities.filter_flights(flight_filters, flight_results)
        self.assertEqual(len(result), 3)

        flight_filters = {"morning-departure": "on"}

        result = flight_utilities.filter_flights(flight_filters, flight_results)
        self.assertEqual(len(result), 21)

        flight_filters = {"afternoon-departure": "on"}

        result = flight_utilities.filter_flights(flight_filters, flight_results)
        self.assertEqual(len(result), 20)

        flight_filters = {"evening-departure": "on"}

        result = flight_utilities.filter_flights(flight_filters, flight_results)
        self.assertEqual(len(result), 7)

        flight_filters = {"afternoon-departure": "on", "airport-BWI": "on"}

        result = flight_utilities.filter_flights(flight_filters, flight_results)
        self.assertEqual(len(result), 3)

        flight_filters = {"morning-departure": "on", "afternoon-arrival": "on"}

        result = flight_utilities.filter_flights(flight_filters, flight_results)
        self.assertEqual(len(result), 7)


class TestGetFlightDetails(unittest.TestCase):
    def test_get_flight_details(self):
        result = flight_utilities.get_flight_details(1, datetime(2024, 10, 10))

        self.assertEqual(
            result,
            {
                "id": 1,
                "origin": "JFK",
                "destination": "LAX",
                "airline": "Celestial Wings",
                "arrival_time": datetime(1900, 1, 1, 11, 30),
                "departure_time": datetime(1900, 1, 1, 8, 0),
                "price": "425.00",
                "num_stops": 0,
                "layover_airports": "",
                "distances": [2469],
            },
        )

        result = flight_utilities.get_flight_details(2, datetime(2024, 10, 10))

        self.assertEqual(
            result,
            {
                "id": 2,
                "origin": "JFK",
                "destination": "LAX",
                "airline": "Skypath Airways",
                "arrival_time": datetime(1900, 1, 1, 13, 45),
                "departure_time": datetime(1900, 1, 1, 9, 15),
                "price": "475.00",
                "num_stops": 1,
                "layover_airports": "(SFO)",
                "distances": [2579, 337],
            },
        )


class TestGetFlightSeatConfiguration(unittest.TestCase):
    def test_get_flight_seat_configuration(self):
        result = flight_utilities.get_flight_seat_configuration(2469)
        self.assertIn(result["name"], ["Aurora A250 Jumbo Jet","Clarion C300 Jumbo Jet"])
        self.assertEqual(result["range"], 3500)
        first_class = result["seat_configuration"]["first_class"]
        self.assertIn(len(first_class), [8,12])
        self.assertEqual(
            first_class[0],
            [
                ["1A","1B"],
                [],
                ["1C", "1D"],
            ],
        )
        economy_class = result["seat_configuration"]["economy_class"]
        self.assertIn(len(economy_class), [36,38])
        self.assertIn(
            economy_class[-1], [[["50A", "50B", "50C"], [], ["50D", "50E", "50F"]],
            [['44A', '44B', '44C'], [], ['44D', '44E', '44F']]]
        )

        result = flight_utilities.get_flight_seat_configuration(8501)
        self.assertIn(result["name"], ["Clarion C600 Wide-Body Jet","Aurora A980 Wide-Body Jet"])
