import unittest
from app.roman_numerals import parse



class TestRomanNumerals():
    def test_i(self):
        value = parse("I")
        assert value == 1

    def test_ii(self):
        value = parse("II")
        assert value == 2

    def test_iii(self):
        value = parse("III")
        assert value == 3

    def test_iii(self):
        value = parse("IV")
        assert value == 4

    def test_iii(self):
        value = parse("V")
        assert value == 5

    def test_iii(self):
        value = parse("VI")
        assert value == 6
