import unittest

import search_bar

class TestSearchBar(unittest.TestCase):
    def test_parse_dates(self):
        query = "May - Jun"
        result = search_bar.parse_dates(query)
        self.assertEqual(result,None)

        query = "May 28 - Jun 5"
        result = search_bar.parse_dates(query)
        self.assertEqual(result,['May 28','Jun 5'])

        # query = "September 1 to 7"
        # result = search_bar.parse_dates(query)
        # self.assertEqual(result, "September 1 to 7")

        # query = "Aug 6"
        # result = search_bar.parse_dates(query)
        # self.assertEqual(result, "Aug 6")

        # query = "October 6, 2023"
        # result = search_bar.parse_dates(query)
        # self.assertEqual(result, "October 6")

        # query = "Nov 7, 2023 - December 4, 2023"
        # result = search_bar.parse_dates(query)
        # self.assertEqual(result, "Nov 7, 2023 - December 4, 2023")

        # query = "Chicago to Austin"
        # result = search_bar.parse_dates(query)
        # self.assertEqual(result, None)
        pass
