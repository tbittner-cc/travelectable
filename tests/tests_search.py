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
