#test if we can filter the right players out
import unittest
from footy import get_players_to_sell


class TestGetPlayersToSell(unittest.TestCase):
    def test_raises_on_non_list(self):
        """
        Test that an exception is raised when anything but a list is passed
        """
        with self.assertRaises(ValueError):
            get_players_to_sell('some fuckery')

    def test_criteria_not_met(self):
        """
        Test that it returns an empty list when no players are about to drop in price
        """
        self.assertEqual(get_players_to_sell([]), [])


