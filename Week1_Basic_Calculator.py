# A simple Python program for basic calculator

# a function to add two numbers
def add(x, y):
    return x + y

# a function to subtract two numbers
def subtract(x, y):
    return x - y

# a function to multiply two numbers
def multiply(x, y):
    return x * y

# a function to divide two numbers
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y


# Getting user input
operation = input("Enter the operation (+, -, *, /): ")
opt1 = float(input("Enter the first number: "))
opt2 = float(input("Enter the second number: "))

# Performing calculations based on user's choice
if operation == "+":
    result = add(opt1, opt2)
elif operation == "-":
    result = subtract(opt1, opt2)
elif operation == "*":
    result = multiply(opt1, opt2)
elif operation == "/":
    result = divide(opt1, opt2)
else:
    result = "Invalid operation!"

# Display result
print(f"{opt1} {operation} {opt2} = {result}")