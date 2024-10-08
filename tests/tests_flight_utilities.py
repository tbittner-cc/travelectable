import unittest
import flight_utilities


class TestRetrieveAirports(unittest.TestCase):
    def test_retrieve_airports(self):
        result = flight_utilities.retrieve_airports((8, 'Boston', 'USA', '(BOS)'))
        self.assertEqual(result,["BOS"])

        result = flight_utilities.retrieve_airports((1,"New York", "USA", "(JFK, LGA, EWR)"))
        self.assertEqual(result,["JFK", "LGA", "EWR"])

class TestGetFlightSearchResults(unittest.TestCase):
    def test_get_flight_search_results(self):
        result = flight_utilities.get_flight_search_results(["JFK","LGA","EWR"],["ORD","MDW"])
        self.assertEqual(len(result),48)

        first_result = result[0]
        self.assertEqual(first_result['origin'], "JFK")
        self.assertEqual(first_result['destination'], "ORD")
        self.assertEqual(first_result['airline'], "AA")
        self.assertEqual(first_result['arrival_time'], "08:30") 
        self.assertEqual(first_result['departure_time'], "06:00")
        self.assertEqual(first_result['layover_airports'], "")
        self.assertEqual(first_result['num_stops'], 0)
