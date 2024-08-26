import unittest
from Calculator import *

class TestCalculation(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.first_number = 12
        cls.second_number = 2

    def test_return_addition(self):
        test_return_input = Addition(self.first_number, self.second_number)
        self.assertEqual(test_return_input, 14, "The sum is incorrect")

    def test_return_subtraction(self):
        test_return_input = Subtraction(self.first_number, self.second_number)
        self.assertEqual(test_return_input, 10, "The subtraction is incorrect")

    def test_return_multiplication(self):
        test_return_input = Multiply(self.first_number, self.second_number)
        self.assertEqual(test_return_input, 24, "The multiplication is incorrect")

    def test_return_division(self):
        test_return_input = Division(self.first_number, self.second_number)
        self.assertEqual(test_return_input, 6, "The division is incorrect")

    def test_return_division_by_zero(self):
        test_return_input = Division(self.first_number, 0)
        self.assertEqual(test_return_input, "Action can not be performe", "The division is incorrect")

if __name__ == '__main__':
    unittest.main()