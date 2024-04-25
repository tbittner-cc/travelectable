import unittest

import dateutil.parser as parser

from main import utilities

class TestGetDates(unittest.TestCase):
    def test_get_dates(self):
        start_date = parser.parse("May 1")
        end_date = parser.parse("May 7")
        
        dates = "May 1-7"
        result = utilities.parse_dates(dates)
        self.assertEqual(result, (start_date, end_date))

        dates = "May 1st-7th"
        result = utilities.parse_dates(dates)
        self.assertEqual(result, (start_date, end_date))
