import re
def get_integer(message: str = "Please enter a number:") -> int:
    """
    This function prompts the user to input an integer and returns it.
    
    Parameters:
    - message (str): The prompt message to display to the user (default is provided).

    Returns:
    - int: The integer entered by the user.
    """
    try:
        input_number = int(input(message))
        return input_number
    except ValueError:
        raise ValueError("Please enter a valid integer")

def get_float(message: str = "Please enter a float:") -> float:
    """
    This function prompts the user to input a float and returns it.
    
    Parameters:
    - message (str): The prompt message to display to the user (default is provided).

    Returns:
    - float: The float entered by the user.
    """
    try:
        input_number = float(input(message))
        return input_number
    except ValueError:
        raise ValueError("Please enter a valid float")

def get_string(message: str = "Please enter a string:") -> str:
    """
    This function prompts the user to input a string and returns it.
    
    Parameters:
    - message (str): The prompt message to display to the user (default is provided).

    Returns:
    - str: The string entered by the user.
    """
    return input(message)

def get_list(message: str = "Please enter a list of items separated by commas:") -> list:
    """
    This function prompts the user to input a list of items separated by commas
    and returns the list.
    
    Parameters:
    - message (str): The prompt message to display to the user (default is provided).

    Returns:
    - list: The list of items entered by the user.
    """
    try:
        input_string = input(message).strip()
        # Split the input string by commas and remove leading/trailing spaces
        pattern = r'\s*(?:,\s*|\s+)*(\d+)\s*'
        input_string = re.split(pattern, input_string)
        input_list = [item for item in input_string if item]
            
        return input_list
    except ValueError:
        raise ValueError("Please enter a valid list")
