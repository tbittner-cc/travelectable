import unittest

import dateutil.parser as parser

from main import utilities

class TestGetDates(unittest.TestCase):
    def test_get_dates(self):
        start_date = "2024-05-01"
        end_date = "2024-05-07"
        
        dates = "May 1-7"
        result = utilities.parse_dates(dates)
        self.assertEqual(result, (start_date, end_date))

        dates = "May 1st-7th"
        result = utilities.parse_dates(dates)
        self.assertEqual(result, (start_date, end_date))

class TestGetSuggestedDates(unittest.TestCase):
    def test_get_suggested_dates(self):
        current_date = parser.parse("2024-05-01")
        result = utilities.get_suggested_dates(current_date)
        self.assertEqual(result, "May 15-21")

        current_date = parser.parse("2024-05-15")
        result = utilities.get_suggested_dates(current_date)
        self.assertEqual(result, "May 29-June 4")

class TestGetLocationDetails(unittest.TestCase):
    def test_get_location_details(self):
        result = utilities.get_location_details("New York")
        self.assertEqual(result, {"city": "Chicago", "latitude": 41.881832, "longitude": -87.623177})

class TestGetHotelOffers(unittest.TestCase):
    def test_get_hotel_offers(self):
        result = utilities.get_hotel_offers()
        self.assertEqual(len(result),10)
        self.assertEqual(result[0]['name'], 'The Langham Chicago')
        # Convert to a string to handle floating point numbers
        self.assertEqual(str(result[2]['distance']), str(0.7))
        self.assertEqual(result[9]['offer_rate'], 80)

class TestGetHotelDetails(unittest.TestCase):
    def test_get_hotel_details(self):
        result = utilities.get_hotel_details()