import unittest
from src.functions import *

class TestFunctions(unittest.TestCase):
    
    def test_add_one__5_returns_6(self):#super clear defined test names
        #3 A's Arrage, Act, Assert
        expected = 6
        actual = add_one(5) #the number I'll get back with the arg used
        self.assertEqual(expected,actual)