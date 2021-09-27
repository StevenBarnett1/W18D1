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

    def test_iv(self):
        value = parse("IV")
        assert value == 4

    def test_v(self):
        value = parse("V")
        assert value == 5

    def test_vi(self):
        value = parse("VI")
        assert value == 6

    def test_vii(self):
        value = parse("VII")
        assert value == 7

    def test_viii(self):
        value = parse("VIII")
        assert value == 8
