import unittest
import mock_data

class TestMockData(unittest.TestCase):
    # This is just testing to ensure that formatting for the room rate function works.
    def test_populate_room_rates(self):
        mock_data.populate_room_rates(17,"Chicago, IL USA")
        