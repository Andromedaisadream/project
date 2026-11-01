import unittest

from calculator import add_numbers
class TestCalculator(unittest.TestCase):
    def test_unsupported_Entry(self):
        with self.assertRaises(TypeError):
            add_numbers("string", 5)