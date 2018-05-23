# This program asks the user for his/her first name and last name
# It then prints out a personalized greeting, depending on the name entered

# We create the 'greet' function
# It takes the first and last names as inputs
# It then prints out a greeting of the form 'Hello, [first_name] [last_name]'
def greet(first_name, last_name):
    print("Hello, {0} {1}".format(first_name, last_name))

# Get the user's first name
fn = input("Enter your first name: ")

# Get the user's last name
ln = input("Enter your last name: ")

# Call the function, which displays the greeting
greet(fn, ln)
