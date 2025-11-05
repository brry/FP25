'''
Hello to Berry or and DH-Master Student that found his/her way here.
If you want, you can play rock, paper, scissors here.
Test change
'''

'''
This is a simple Rock, Paper, Scissors game where the user plays against the computer.
It also uses ascii art to represent the choices.
'''

import random

# Ascii Art:

# Rock
Rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
Paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
Scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

print("Welcome to Rock, Paper, Scissors!")
print("Make your choice:")
user_choice = int(input("Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))

print("You chose:")
if user_choice == 0:
    print("Rock")
    print(Rock)
elif user_choice == 1:
    print("Paper")
    print(Paper)
elif user_choice == 2:
    print("Scissors")
    print(Scissors)


# Generate a random choice for the computer

computer_choice = random.randint(0, 2)
print("Computer chose:")
if computer_choice == 0:
    print("Rock")
    print(Rock)
elif computer_choice == 1:
    print("Paper")
    print(Paper)
elif computer_choice == 2:
    print("Scissors")
    print(Scissors)

# Determine the winner

# When the user chooses rock
if user_choice == 0 and computer_choice == 2:
    print("You win!")
elif user_choice == 0 and computer_choice == 1:
    print("You lose!")
elif user_choice == 0 and computer_choice == 0:
    print("It's a draw!")

# When the user chooses paper
if user_choice == 1 and computer_choice == 0:
    print("Congrats! You win!")
elif user_choice == 1 and computer_choice == 2:
    print("Oh no! You lose!")
elif user_choice == 1 and computer_choice == 1:
    print("It's a draw!")

# When the user chooses scissors
if user_choice == 2 and computer_choice == 1:
    print("You win!")
elif user_choice == 2 and computer_choice == 0:
    print("You lose!")
elif user_choice == 2 and computer_choice == 2:
    print("It's a draw!")

# When the user chooses an invalid option
if user_choice < 0 or user_choice > 2: 
    print("Invalid choice! Choose a value beteween 0 and 2.")   
