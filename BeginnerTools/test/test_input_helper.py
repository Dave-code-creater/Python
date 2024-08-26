import unittest
from unittest.mock import patch
from src.input_helper import get_integer, get_float, get_string, get_list

class TestInputHelper(unittest.TestCase):
    @patch('builtins.input', return_value='5')
    def test_get_integer_valid_input(self, mock_input):
        self.assertEqual(get_integer("Please enter an integer"), 5)
        
    @patch('builtins.input', return_value='invalid')
    def test_get_integer_invalid_input(self, mock_input):
        with self.assertRaises(ValueError):
            get_integer("Please enter an integer")
    
    @patch('builtins.input', return_value='5.5')
    def test_get_float_valid_input(self, mock_input):
        self.assertEqual(get_float("Please enter a float"), 5.5)
        
    @patch('builtins.input', return_value='invalid')
    def test_get_float_invalid_input(self, mock_input):
        with self.assertRaises(ValueError):
            get_float("Please enter a float")
            
    @patch('builtins.input', return_value='hello')
    def test_get_string_valid_input(self, mock_input):
        self.assertEqual(get_string("Please type a string"), 'hello')
        
    # No need for an invalid test case for get_string as it doesn't raise an error
    
    @patch('builtins.input', return_value='1,2,3')
    def test_get_list_valid_input(self, mock_input):
        self.assertEqual(get_list("Please enter a list"), ['1', '2', '3'])
        
    @patch('builtins.input', return_value='1 2 3')
    def test_get_list_valid_input_with_spaces(self, mock_input):
        self.assertEqual(get_list("Please enter a list"), ['1', '2', '3'])
        
    # Assuming get_list function does not raise ValueError for invalid inputs
    # and handles comma-separated lists correctly
    
if __name__ == "__main__":
    unittest.main()
