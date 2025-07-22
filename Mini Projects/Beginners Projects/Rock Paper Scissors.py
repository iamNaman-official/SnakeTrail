# The Rock Paper scissors game code :


Rock = '''---'   ____)
      (_____)
      (_____)
      (____)
---.__(___) '''

Paper = '''---'   ____)____
          ______)
          _______)
         _______)
---.__________) '''

Scissors = '''    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)'''




print("Welcome to the Rock Paper Scissors game!")
print("Type 0 for Rock, 1 for Paper, or 2 for Scissors and press Enter: ")
import random
user_choice = int(input("Enter the number corresponding to your choice: "))
print(choices[user_choice])  # Displays the user's choice using the game images.
choices = [Rock , Paper , Scissors]
computer_choice = random.randint(0, 2)  # Randomly selects a choice for the computer.
print(choices[computer_choice])  # Displays the computer's choice using the game images.
print(f"You chose: {choices[user_choice]}")
print(f"Computer chose: {choices[computer_choice]}")
if user_choice == computer_choice:
    print("It's a tie!")
elif (user_choice == 0 and computer_choice == 2) or \
     (user_choice == 1 and computer_choice == 0) or \
     (user_choice == 2 and computer_choice == 1):  # Conditions for user win.
    print("You win! Congratulations!")
elif (computer_choice == 0 and user_choice == 2) or \
     (computer_choice == 1 and user_choice == 0) or \
     (computer_choice == 2 and user_choice == 1):  # Conditions for computer win.
    print("Computer wins! Better luck next time!")
else :
    print("You lose! Better luck next time.")                