# Read the assigment
# 1. Write a function to handle the addition of two number
# 2. Write another function to handle the substraction
# 3. Write a function to handle multiplication
# 4. Write a function to handle division

def Addition(first_number, second_number) -> int:
    ##TODO: Write a function to handle the addition of two number

def Subtraction(first_number, second_number) -> int:
    # TODO: Write another function to handle the substraction

def Multiply(first_number, second_number) -> int:
    # TODO: Write a function to handle multiplication

def Division(first_number, second_number) -> int:
    # TODO: Write a function to handle division

def main():
    First_Number = int(input("Please input the first value of the first number: "))
    Second_Number = int(input("Please input the second number: "))
    Action = input("Please input the operand you want to perfom: ")

    if Action == "+":
        result = Addition(First_Number, Second_Number)
    elif Action == "-":
        result = Subtraction(First_Number, Second_Number)
    elif Action == "*":
        result = Multiply(First_Number, Second_Number)
    elif Action == "/":
        result == Division(First_Number, Second_Number)

    else:
        print("Invalid input")

    print(f"{First_Number} {Action} {Second_Number} = {result}")

if __name__ == "__main__":
    main()