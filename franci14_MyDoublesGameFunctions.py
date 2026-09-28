# franci14_MyDoublesGameFunctions.py
# Jacob S. Francis
# GEO 443 - Python Programming
# This is my program for practicing simple functions
# This program plays the Doubles math game!
# 02/06/2026
# print statements moved from outside the function to avoid them
# printing again on the 2nd and 3rd user input
print("Welcome to the math doubles game!")
print("You get to choose the number you want doubled!")


# This first function will print out basic instructions for the doubling game
def instructions():
    return int(input("Type in a number: "))


# This next function does the doubling of the integer
def double(x):
    print("Doubles! Doubles! I can add doubles - It's no trouble for me to \
add doubles!")
    print(x, "+", x, "equals", x + x, "!")


# Call the instructions function and put a return value into a new variable
# Which we are defining as 'number'
number = instructions()
# Now we will call the double function and use number as the required input
double(number)

# Now that the function has been used, it can be run in the same program
# multiple times. For the next part of the assignment, we will call the
# function 2 more times so that the user would be able to play the game
# multiple times. Looping and conditionals will become available and useful
# for this in the next assignment!
# print statement for the next user input, call the functions again
# by defining number_2 as a new variable in the instructions() return value
print("Now, choose another number you want to double!")
number_2 = instructions()
double(number_2)
# repeat the above print and function call for a new variable number_3
print("Now, choose a third number you want to double!")
number_3 = instructions()
double(number_3)
