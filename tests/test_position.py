import unittest
from functools import wraps
from src.positions import Positions


class TestPosition(unittest.TestCase):

    @staticmethod
    def build_custom_assertion(func):
        @wraps(func)
        def inner(*args, **kwargs):
            try:
                func(*args, **kwargs)
            except KeyError:
                return False
            else:
                return True
        return inner 

    @build_custom_assertion
    def __test_positions(self, position):
        Positions.__getitem__(position)

    def test_allowed_position(self):
        Positions.__getitem__("MIDFIELDER")

    def test_all_positions(self):
        positions = {
            "DEFENDER": True, 
            "GOALKEEPER": True,
            "GOAL": False, 
            "PILOT": False, 
            "FORWARD": True}
        for position, is_allowed in positions.items():
            r = self.__test_positions(position)
            self.assertEqual(r, is_allowed)

