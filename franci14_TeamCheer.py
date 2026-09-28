# franci14_TeamCheer.py
# Jacob S. Francis
# GEO 443A - Python Programming
# Script to cheer for users favorite team, using the FOR LOOP.
# This script also uses the upper() function for strings
# 02/09/2026
# Welcome message and blank line to format
print("Welcome to the Team Cheer Game!")
print("")
# team variable set to whatever the user inputs
# print statement asking their favorite team
team = input("What is the name of your favorite team?")
# now we have the name stored, it needs to convert to letters txt
letters = list(team)
# for the actual letter in letters, print "Give me a" --- uppercase letter
for letter in letters:
    print("Give me a", letter.upper(), "!")

# second part of the cheer
# includes the team variable for the full name of the team
print("What does that spell?")
print(team.upper(), "!")
