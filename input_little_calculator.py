# franci14
# input_little_calculator.py
# Input function program that shows how to work with numbers
# 2/1/2026
print("Hello and Welcome to my Little Calculator.")
print("This calculator will ask you for a number and then tell you the \
square of the number.")
# Method 1 - Place the input statement in the INT()
number = int(input("Please type in the number you want to square:"))
number_sqr = number * number
print("The square of", number, "is", number_sqr)
# Method 2 -Placing the variable holding the input to the INT()
number2 = input("Please enter another number to square:")
number2_sqr = int(number2) * int(number2)
print("The square of", number2, "is", number2_sqr)
