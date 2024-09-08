import unittest
from datetime import datetime
import utilities

class TestIsWinterRate(unittest.TestCase):
    def test_is_winter_rate(self):
        result = utilities.is_winter_rate(datetime(2024, 4, 1))
        self.assertEqual(result, True)

        result = utilities.is_winter_rate(datetime(2024, 5, 1))
        self.assertEqual(result, False)

        