import unittest
from datetime import datetime
import dateutil.parser as parser
import utilities

class TestGetDates(unittest.TestCase):
    def test_get_dates(self):
        start_date = datetime(2024, 5, 1)
        end_date = datetime(2024, 5, 7)
        
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

class TestIsWinterRate(unittest.TestCase):
    def test_is_winter_rate(self):
        result = utilities.is_winter_rate(datetime(2024, 4, 1))
        self.assertEqual(result, True)

        result = utilities.is_winter_rate(datetime(2024, 5, 1))
        self.assertEqual(result, False)

class TestGetHotelsWithAmenities(unittest.TestCase):
    def test_get_hotels_with_amenities(self):
        result = utilities.get_hotels_with_amenities([{'id':17},{'id':20},{'id':22}],"wifi",'')
        