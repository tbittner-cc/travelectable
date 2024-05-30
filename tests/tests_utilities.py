import unittest
import dateutil.parser as parser
import utilities

class TestGetDates(unittest.TestCase):
    def test_get_dates(self):
        start_date = "2024-05-01"
        end_date = "2024-05-07"
        
        dates = "May 1-7"
        result = utilities.parse_dates(dates)
        self.assertEqual(result, (start_date, end_date))

        dates = "May 1 - 7"
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
        result = utilities.is_winter_rate("2024-04-01")
        self.assertEqual(result, True)

        result = utilities.is_winter_rate("2024-05-01")
        self.assertEqual(result, False)

class TestGetHotels(unittest.TestCase):
    def test_get_hotels(self):
        result = utilities.get_hotels((3,"Chicago, IL USA"))
        hotel_names = [row["name"] for row in result]
        self.assertIn("Hilton Chicago", hotel_names)

class TestGetLeadRates(unittest.TestCase):
    def test_get_lead_rates(self):
        result = utilities.get_lead_rates([{'id':17},{'id':20},{'id':22}],"2024-05-01")
        self.assertEqual(result, [(17,'350'),(20,'219'),(22,'229')])

        result = utilities.get_lead_rates([{'id':17},{'id':20},{'id':22}],"2024-11-01")
        self.assertEqual(result, [(17,'250'),(20,'139'),(22,'159')])

        result = utilities.get_lead_rates([{'id':0}],"2024-12-01")
        self.assertEqual(result, [(0,'')])

class TestGetSelectedLocations(unittest.TestCase):
    def test_get_selected_locations(self):
        result = utilities.get_selected_locations({'origin':'','destination':''},[(3,'Chicago, IL USA')])
        self.assertEqual(result, ['',''])

        result = utilities.get_selected_locations({'origin':'Chicago, IL USA','destination':''},[(3,'Chicago, IL USA')])
        self.assertEqual(result, [(3,'Chicago, IL USA'),''])

        result = utilities.get_selected_locations({'origin':'','destination':'Chicago, IL USA'},[(3,'Chicago, IL USA')])
        self.assertEqual(result, ['',(3,'Chicago, IL USA')])

        result = utilities.get_selected_locations({'origin':'Chicago, IL USA','destination':'New York, NY USA'},
                                                    [(1,'New York, NY USA'),(3,'Chicago, IL USA')])
        self.assertEqual(result, [(3,'Chicago, IL USA'),(1,'New York, NY USA')])
        