# Write a program that prompts the user for two numbers and then prints the sum of those numbers.


def add(a: float, b: float) -> float:
    """
    Adds two floating-point numbers and returns the result.

    Args:
        a (float): The first number to add.
        b (float): The second number to add.

    Returns:
        float: The sum of the two numbers.
    """
     # TODO: Implement this function that return a + b
    pass

def substract(a: float, b:float) -> float:
    """
    Substracts two floating-point numbers and returns the result.

    Args:
        a (float): The first number to substract.
        b (float): The second number to substract.

    Returns:
        float: The difference of the two numbers.
    """
    # TODO: Implement this function that return a - b
    pass

def multiply(a: float, b: float) -> float:
    """
    Multiplies two floating-point numbers and returns the result.

    Args:
        a (float): The first number to multiply.
        b (float): The second number to multiply.

    Returns:
        float: The product of the two numbers.
    """
    # TODO: Implement this function that return a * b
    pass

def divide(a: float, b: float) -> float:
    """
    Divides two floating-point numbers and returns the result.

    Args:
        a (float): The first number to divide.
        b (float): The second number to divide.

    Returns:
        float: The quotient of the two numbers.
    """
    # TODO: Implement this function that return a / b
    # REMEBER: You should return 0 if the second number is zero
    pass

def main():
    a, b = float(input("Enter the first number: ")), float(input("Enter the second number: "))
    print(f"The sum of {a} and {b} is {add(a, b)}")
    print(f"The difference of {a} and {b} is {substract(a, b)}")
    print(f"The product of {a} and {b} is {multiply(a, b)}")
    print(f"The quotient of {a} and {b} is {divide(a, b)}")
   