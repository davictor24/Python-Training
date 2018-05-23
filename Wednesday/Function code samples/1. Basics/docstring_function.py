# We create a function that contains a docstring

# Docstrings are string literals that occur as the first statement in a
# function, module, class or method definition

# They can be used to give more information about the function
# Most IDEs allow you to inspect the docstring of functions
# thereby giving insight as to how to use the function, or what it does

# They are created using triple single or double quotes
# This is similar to how multi-line comments are created

def square(x):
    '''
    This function takes a numeric input, x
    and returns its square, x**2
    '''
    return x**2

print(square(149)) # prints 22201
