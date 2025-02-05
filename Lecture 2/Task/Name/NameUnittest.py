import unittest
from io import StringIO
from unittest.mock import patch
import Name
from datetime import date

class TestName(unittest.TestCase):
    """
    A test case for testing the 'name_test' method.
    """

    def name_test(self, input, expected_output):
        """
        Test the 'name_test' method by simulating user input and checking the output.

        Args:
            input (list): The list of user inputs to simulate.
            expected_output (str): The expected output to compare against.

        Raises:
            AssertionError: If the output does not match the expected output.
        """
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            with patch('builtins.input', side_effect=input):
                try:
                    self.assertEqual(fakeOutput.getvalue().strip(), expected_output)
                except AssertionError:
                    self.fail("There is no output.")

    def test_type(self):
        """
        Test the type of the 'name' variable.

        Raises:
            AttributeError: If the 'name' variable is not defined.
        """
        try:
            self.assertEqual(type(Name.name), str)
        except AttributeError:
            self.fail("The variable 'name' is not defined.")

    def _steps(self):
        """
        Generator function to iterate over all step methods in the test case.

        Yields:
            tuple: A tuple containing the name and reference to each step method.
        """
        for name in dir(self): # dir() result is implicitly sorted
            if name.startswith("step"):
                yield name, getattr(self, name) 

    def test_steps(self):
        """
        Test each step method in the test case.

        Raises:
            Exception: If any step method fails.
        """
        for name, step in self._steps():
            try:
                step()
            except Exception as e:
                self.fail("{} failed ({}: {})".format(step, type(e), e))

def Write_Log():
    """
    Writes log information to a file.

    This function appends the current date, a log message, and the result of running
    a unit test case to a log file named "log.txt". If all test cases pass, it writes
    "All test cases passed." Otherwise, it writes the names of the failed test cases.

    Parameters:
    None

    Returns:
    None
    """
    date_run = date.today()
    with open("log.txt", "a") as file:
        file.write(date_run.strftime("%m/%d/%Y") + "\n")
        file.write("This is a log file.\n")
        result = unittest.TextTestRunner().run(unittest.defaultTestLoader.loadTestsFromTestCase(TestName))
        if result.wasSuccessful():
            file.write("All test cases passed.\n")
        else:
            file.write("Failed test cases:\n")
            for failure in result.failures:
                file.write(failure[0]._testMethodName + "\n\n")

if __name__ == "__main__":
    Write_Log()

