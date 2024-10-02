import unittest
from datetime import datetime
import utilities

class TestIsWinterRate(unittest.TestCase):
    def test_is_winter_rate(self):
        result = utilities.is_winter_rate(datetime(2024, 4, 1))
        self.assertEqual(result, True)

        result = utilities.is_winter_rate(datetime(2024, 5, 1))
        self.assertEqual(result, False)

class TestGetLeadRates(unittest.TestCase):
    def test_get_lead_rates(self):
        # #Hotel 61 is in New York
        # #Hotel 1791 is in Tokyo 
        hotels = [
            {
                'id': 61,},
            {
                'id': 1791,},
        ]
        result = utilities.get_lead_rates(hotels,datetime(2024, 5,1))
        self.assertEqual(result, [(61,400),(1791,153)]) 

class TestConvertRatesToUSD(unittest.TestCase):
    def test_convert_rates_to_usd(self):
        result = utilities.convert_rates_to_usd(
            [(1,100,10),(1,200,10),(1,300,10),(1,400,10),
             (2,500,10),(2,600,10),(2,700,10),(2,1000,10),
             (3,1200,10),(3,1300,10),(3,1400,10),(3,1500,10),
             (4,500,100),(4,600,100),(4,1700,100),(4,10000,100)])

        self.assertEqual(result, [
            (1,100),(1,200),(1,300),(1,400),
            (2,500),(2,600),(2,700),(2,1000),
            (3,120),(3,130),(3,140),(3,150),
            (4,5),(4,6),(4,17),(4,100)])

class TestGetHotelDetails(unittest.TestCase):
    def test_get_hotel_details(self):
        result = utilities.get_hotel_details((1,"New York"),(datetime(2024,5,1),datetime(2024,5,1)),61,False)
        self.assertEqual(result['name'],"The Empire Hotel")
        self.assertEqual(len(result['rates']),4)

        rates = sorted([rate['summer_rate'] for rate in result['rates']])
        self.assertEqual(rates,[400,500,800,1200])

        result = utilities.get_hotel_details((87,"Tokyo"),(datetime(2024,5,1),datetime(2024,5,1)),1791,False)
        self.assertEqual(result['name'],"Shinagawa Grand Hotel")
        self.assertEqual(len(result['rates']),4)

        rates = sorted([rate['summer_rate'] for rate in result['rates']])
        self.assertEqual(rates,[153,244,335,489])