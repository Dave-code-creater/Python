import unittest
from Calculator import Addition

class TestCalculation(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.first_number = 2
        cls.second_number = 12

    def test_return_addition(self):
        test_return_input = Addition(self.first_number, self.second_number)
        print(test_return_input)
        self.assertEqual(test_return_input, 13, "The sum is incorrect")

    def test_return_subtraction():
        pass

if __name__ == '__main__':
    unittest.main()