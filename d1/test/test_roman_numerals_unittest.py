import unittest
from app.roman_numerals import parse



class TestRomanNumerals:
    def __init__(self):
        pass
    def test_i(self):
        value = parse("I")
        self.assertEqual(value, 1)
