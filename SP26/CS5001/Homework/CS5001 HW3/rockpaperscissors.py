# CS 5001, Assignment #3 Rock, Paper, Scissors Game
# DO NOT use AI tools while working on this assignment.
# I confirm that AI code completion tools were disabled while writing this program
# NEUID: 003163519 
# Name: Ryu Hemingway
#adding this for my github commit

import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
_______
---'   ____)____
            ______)
            _______)
            _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
            ______)
         __________)
      (____)
---.__(___)
"""

# TO DO: Print the title of the game and/or welcome message
print("Welcome to the Rock-Paper-Scissors game!")

# TO DO: Prompt the user for input (0, 1, 2)
# Ask for user input and we are asked to make the choices into a list format
user_input = int(input("What is your choice?"))

game_images = [rock, paper, scissors]

# TO DO: Print ASCII art for user's choice
# Print the user art depending on choice
if user_input >= 0 and user_input <= 2:
    print(game_images[user_input])

# TO DO: Generate computer choice
# Run the random function
    comp_input = random.randint(0,2)

    # TO DO: Print ASCII art for computer's choice
    # Print the computers art depending on its choice
    print("Computer chose: ")
    print (game_images[comp_input])

    # TO DO: Decide winner using conditionals
    # Here is the core logic, i left until the end becuase python needs to have the information before running the if/elif/else logic
    if user_input == comp_input:
        print("It is a tie!")
    elif (user_input == 0 and comp_input == 2) or (user_input == 1 and comp_input == 0) or (user_input == 2 and comp_input == 1):
        print("You win!")
    else:
        print("You lose!")
else:
    print("Invalid input, please try again")

# I nested the final else statement incase the user inputs anything other than [0,2]

