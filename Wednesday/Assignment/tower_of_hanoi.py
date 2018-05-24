# We create a function to solve the problem
# This function will be called recursively
# n is number of discs
# pole_from is the pole number from which we want to transfer
# pole_to is the pole number to which we want to transfer
# pole_helper is a helper pole
def solve(n, pole_from, pole_to, pole_helper): 
    if n == 1:# Base case of the recursion
        # Simply move from the source to the destination
        print("Move from pole {0} to pole {1}".format(pole_from, pole_to))
        
    else:# Use recursion to solve a smaller problem
        # Move the items above the last disc to the helper pole
        # There are n-1 items above, so we are working with a simpler version of the problem
        # Use the destination as a helper
        solve(n-1, pole_from, pole_helper, pole_to)

        # Move the last item left at the source directly to the destination
        print("Move from pole {0} to pole {1}".format(pole_from, pole_to))

        # Move all items still at the helper pole to the destination
        # There are n-1 items, so we are working with a simpler version of the problem
        # Use the source as a helper
        solve(n-1, pole_helper, pole_to, pole_from)

num_discs = int(input("Enter number of discs: ")) # Gets number of discs
solve(num_discs, 1, 3, 2) # Calls the function and runs the algorithm
