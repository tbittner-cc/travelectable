import unittest

from main import hotel_fns

class TestCreateHotelRatingsSublists(unittest.TestCase):
    def test_create_hotel_ratings_sublists(self):
        hotel_ids = [1,2,3,4,5,6,7,8,9,10]
        self.assertEqual(hotel_fns.create_hotel_ratings_sublists(hotel_ids), 
                         [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10]])