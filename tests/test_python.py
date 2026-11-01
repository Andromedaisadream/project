import unittest

from calculator import add_numbers

class TestCalculator(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(add_numbers(606060, 4000), 610060)

    def test_negative(self):
        self.assertEqual(add_numbers(-100, -400), -500)
