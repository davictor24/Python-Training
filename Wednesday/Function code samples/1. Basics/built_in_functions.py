# We will experiment with some built in functions in Python
# We have encountered a number of them. Some of them include:
# - print()
# - input()
# - range()
# - type()
# - str()
# - float()
# - list()
# - len(), e.t.c
# Let's look at some more

arr = [2, 0, 7, -1, 3]

# 'max' get the maximum item in an array
print(max(arr)) # prints 7

# 'min' gets the minimum item in an array
print(min(arr)) # prints -1

# 'sum' gets the sum of items in an aray
print(sum(arr)) # prints 11

# 'abs' gets the absolute value of a number
print(abs(-13)) # prints 13

# 'hex' converts a number to hexadecimal, beginning with '0x'
print(hex(46)) # prints 0x2e

# To use math functions, import the math module
import math

# 'math.log' gives the natural logarithm of a number
print(math.log(2)) # prints 0.69314718...

# 'math.log10' gives the base 10 logarithm of a number
print(math.log10(100)) # prints 2.0

# For all trigonometric functions (such as shown below), angles are in radians

# 'math.sin' gives the sine of a number
# 'math.pi' represents pi
print(math.sin(math.pi / 2)) # returns 1.0 (since sin(pi/2) = 1)

# 'math.acos' gives the arc cosine (inverse cosine) of a number
print(math.acos(-1)) # returns 3.1415926... (= pi, since cos(pi) = -1)

