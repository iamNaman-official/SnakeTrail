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

choices = [Rock , Paper , Scissors]
choices_names = ["Rock", "Paper", "Scissors"]
# Welcoming to the game and instructions for the user.
print("Welcome to the Rock Paper Scissors game!")
print("Type 0 for Rock, 1 for Paper, or 2 for Scissors and press Enter: ")

# The user is prompted to enter their choice.
import random
user_choice = input("Enter the number corresponding to your choice: ")
if user_choice.isdigit():
    user_choice = int(user_choice)  # Converts the input to an integer.
    if user_choice in [0, 1, 2]:  # Validates the user's choice.
       print(f"You chose: {choices_names[user_choice]}")  # Displays the user's choice using the game images.
       print(f"You chose: {choices[user_choice]}")
    else:
      print("Invalid input! Please enter a number between 0 and 2.")
      exit()  
else:
    print("Invalid input! Please enter a number between 0 and 2.")
    exit()

# The computer randomly selects a choice from the available options.
computer_choice = random.randint(0, 2)  # Randomly selects a choice for the computer.
print(f"Computer chose: {choices_names[computer_choice]}")  # Displays the computer's choice using the game images.
print(f"Computer chose: {choices[computer_choice]}")

# The game logic to determine the winner.
# The game rules are applied to determine the winner based on the choices made by the user and computer.
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
print("Thank you for playing Rock Paper Scissors!")  # Ending message for the game.
print("Goodbye!")  # Farewell message after the game ends.  
# The code implements a simple Rock Paper Scissors game where the user plays against the computer.
# The user inputs their choice, and the computer randomly selects its choice.
# The game then determines the winner based on the rules of Rock Paper Scissors.