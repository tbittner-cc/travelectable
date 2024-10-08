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
        self.assertEqual(len(result),6)

        first_result = result[0]
        self.assertEqual(first_result['origin'], "JFK")
        self.assertEqual(first_result['destination'], "ORD")
        self.assertEqual(len(first_result['flight_options']),8)

        first_flight_option = first_result['flight_options'][0]
        self.assertEqual(first_flight_option, {'airline':'AA','arrival_time':'08:30',
            'departure_time':'06:00','layover_airports':'','num_stops':0,'price':'250.00'})