import unittest
from compute import NumberInput, Calculator

class TestCalculator(unittest.TestCase):
    def test_add(self):
        first = 12
        second = 10
        result = Calculator().add(first,second)
        self.assertEqual(result, 22)

    def test_add_fail(self):
        first = 12
        second = 10
        result = Calculator().add(first, second)
        self.assertIsNot(result, 21)

    def test_subtract(self):
        first = 12
        second = 10
        result = Calculator().subtract(first, second)
        self.assertEqual(result, 2)

    def test_subtract_fail(self):
        first = 12
        second = 10
        result = Calculator().add(first, second)
        self.assertIsNot(result, 2)

if __name__ == '__main__':
    unittest.main()