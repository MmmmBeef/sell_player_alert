# Test that the function to get football data works
import unittest
from footy import get_football_data, FOOTY_URL
from test.common import VALID_RESULTS, EMPTY_RESULTS
import requests_mock
from json import JSONDecodeError


class TestGetFootballData(unittest.TestCase):
    """
    Test that the football JSON is parsed and returned
    """

    @requests_mock.mock()
    def test_fails_to_retrieve_valid_json(self, mocked_request):
        """
        Test that when the request fails to get the data that an exception is raised
        """
        mocked_request.get(FOOTY_URL, text="Internal Server Error")
        with self.assertRaises(JSONDecodeError):
            get_football_data()

    @requests_mock.mock()
    def test_retrieves_data(self, mocked_request):
        """
        Test that when the request gets data that the list of players is returned
        """
        mocked_request.get(FOOTY_URL, text=VALID_RESULTS)
        players = get_football_data()
        self.assertEqual(len(players), 1)
        self.assertEqual(players[0][2], 'Arsenal')

    @requests_mock.mock()
    def test_retrieve_empty_list(self, mocked_request):
        """
        Test that when the request gets an empty list of data that an exception is raised
        """
        mocked_request.get(FOOTY_URL, text=EMPTY_RESULTS)
        with self.assertRaises(ValueError):
            get_football_data()

