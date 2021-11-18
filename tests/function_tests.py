import unittest
from src.functions import *


class TestFunctions(unittest.TestCase):
    def test_add_one__5_returns_6(self):  # super clear defined test names
        # 3 A's Arrage, Act, Assert
        expected = 6
        actual = add_one(5)  # the number I'll get back with the arg used
        self.assertEqual(expected, actual)

    def test_compare__3_is_greater_than_one(self):
        expected = "first number greater than"
        actual = compare(3, 1)
        self.assertEqual(expected, actual)

    def test_compare__3_is_less_than_5(self):
        expected = "first number less than"
        actual = compare(3, 5)
        self.assertEqual(expected, actual)
        
    def test_compare__3_is_equal_to(self):
        expected = "first number equal to"
        actual = compare(3, 3)
        self.assertEqual(expected, actual)

