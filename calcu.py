import operator
from termcolor import colored
import pyfiglet

# define a function for performing the calculations
def calculate():
    try:
        # ask the user for two numbers and an operation
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Choose an operation (+, -, *, /): ")
        
        # perform the calculation based on the chosen operation
        if operation == "+":
            result = operator.add(num1, num2)
        elif operation == "-":
            result = operator.sub(num1, num2)
        elif operation == "*":
            result = operator.mul(num1, num2)
        elif operation == "/":
            result = operator.truediv(num1, num2)

        # print the result of the calculation
        print(colored(pyfiglet.figlet_format("Result"), color="green"))
        print(colored(f"{result:.2f}", color="green"))
    except ValueError:
        # handle errors when the user enters invalid input
        print(colored(pyfiglet.figlet_format("Error"), color="red"))
        print("Please enter valid numbers")
    except ZeroDivisionError:
        # handle errors when the user tries to divide by zero
        print(colored(pyfiglet.figlet_format("Error"), color="red"))
        print("Cannot divide by zero")

# repeatedly ask the user to perform calculations
while True:
    calculate() # call the calculate function
    choice = input("Do you want to try again? (y/n): ")
    if choice.lower() == "n":
        print(colored(pyfiglet.figlet_format("Thank you!"), color="blue"))
        break
    elif choice.lower() != "y":  # added an error if the user inputs something other than y or n
        print(colored(pyfiglet.figlet_format("Error"), color="red"))
        print("Invalid input. Please enter either 'y' or 'n'")
