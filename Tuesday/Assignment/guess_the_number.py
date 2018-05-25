# import the 'random' module
import random

# The computer guesses a random number between 1 and 100
num = random.randint(1, 100)

print("I have chosen a random number between 1 and 100.")

# Create flag variable which would hold the current game state
# A flag variable, in basic terms, is a boolean variable
# 'gotAnswer' will be true if you have gotten the answer, and false otherwise
# This would be useful when the loop terminates
# An alternative however, would be to use a for...else statement
gotAnswer = False

for i in range(1, 11): # loop runs 10 times, unless a break occurs
    guess = int(input("What is your guess?: ")) # prompt
    
    if num == guess: # you got the answer
        # Print text, set 'gotAnswer' to true, and break
        print("Congratulations! " + str(num) + " is my number.")
        print("You got it after " + str(i) + " trials.")
        gotAnswer = True
        break
    
    elif num > guess: # you guessed too small
        print("Greater than " + str(guess) + ". Try again.")
        
    else: # you guessed too high
        print("Less than " + str(guess) + ". Try again.")

    # Prints number of trials left, if a break doesn't occur
    print("You have " + str(10 - i) + " trials left.")

# If gotAnswer == False, you didn't get the answer
# Since you have exhausted your trials, the answer is printed out
# As said above, a better alternative would be to use a for...else statement
if not gotAnswer: # if 'gotAnswer' is false, 'not gotAnswer' is true
    print("You have exhausted all your trials.")
    print("My number is " + str(num))
