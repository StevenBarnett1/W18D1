import unittest
from app.roman_numerals import parse



class TestRomanNumerals():
    def test_i(self):
        value = parse("I")
        assert value == 1

    def test_ii(self):
        value = parse("II")
        assert value == 2
