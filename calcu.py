import operator

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
        
        # handle errors when the user enters invalid input
        
        # handle errors when the user tries to divide by zero

# repeatedly ask the user to perform calculations