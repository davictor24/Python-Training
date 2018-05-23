# This program takes two numbers and displays their sum

# First, we create the add_numbers function
# It takes two inputs, x and y
# It then returns the sum to the calling process
# The 'return' statement is used to return data from a function
def add_numbers(x, y):
    return x + y

# Get first number
a = float(input("Enter first number: "))

# Get second number
b = float(input("Enter second number: "))

# Compute sum
s = add_numbers(a, b)

# Print sum
print(s)
