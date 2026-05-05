# This is my password generator project.
# It generates a random password based on user input for length and character types.
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Easy level :
# password = ""

# for char in range(1 , nr_letters + 1):
#     random_letter= random.choice(letters)
#     password += random_letter

# for char in range(1 , nr_symbols + 1):
#     password += random.choice(symbols)

# for char in range(0 , nr_numbers): # Changed range to start from 0 because it will start from 0 index to the desired number
#     password += random.choice(numbers)
# print(f"Your password is: {password}")

# Hard level :
password_list =[]

for char in range(0 , nr_letters):
    password_list.append(random.choice(letters))

for char in range(0, nr_symbols):
    password_list.append(random.choice(symbols))

for char in range(0 , nr_numbers): # Changed range to start from 0 because it will start from 0 index to the desired number
    password_list.append(random.choice(numbers))

print(f"Your password is: {password_list}")
random.shuffle(password_list)  # Shuffle the list to make the password more random
print(f"Your shuffled password is:{password_list}")

password = ""
for char in password_list:
    password += char

print(f"Your password is: {password}")  # Print the final password as a string.
print(f"Your password length is: {len(password)} characters.")  # Print the length of the password.
print("Thank you for using the PyPassword Generator!")  # Thank the user for using the generator.

