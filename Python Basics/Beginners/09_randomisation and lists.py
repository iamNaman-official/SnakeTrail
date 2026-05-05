# This is a simple Python script to demonstrate the use of modules and randomization.
# Importing the random module to generate random numbers.
import random
random_number = random.randint(1, 100)  # Generates a random number between 1 and 100.
print(f"Random number generated: {random_number}")

# How to create and use a custom module.
# This module can be used to store and retrieve a favorite number.
import my_module  # Importing the custom module.
print(f"My favourite number is: {my_module.my_favourite_number}")  

# Functions in randomization.
import random
random_number = random.random()  # Generates a random float between 0.0 and 1.0.
print(f"Random float generated: {random_number}")

import random
random_number = random.random()*10 # Generates a random float between 0.0 and 1.0.
print(f"Random float generated: {random_number}")

import random
random_float = random.uniform(1, 10)  # Generates a random float between 1.0 and 10.0.
print(f"Random float between 1 and 10 : {random_float}")

# Example of heads or tails using randomization.
import random
random_heads_or_tails = random.randint(0, 1)  # Generates a random integer, either 0 or 1.
if random_heads_or_tails == 0:
    print("Heads")
else:
    print("Tails")    

# Python Lists :
fruits =["Apple", "Banana", "Cherry", "Date"]
print(fruits[0])
fruits[3] = "Dragonfruit"  # Changing the last element of the list.
print(fruits)

# Adding an element to the list.
fruits.append("Elderberry")  # Appending a new fruit to the list.
print(fruits)

# Extending the list with another list.
vegetables = ["Carrot", "Broccoli"]
fruits.extend(vegetables)  # Adding vegetables to the fruits list.  
print(fruits)

# example :
import random
friends = ["Alice", "Bob", "Charlie", "David"]
random_friend = random.choice(friends)  # Randomly selects a friend from the list.
print(f"Randomly selected friend: {random_friend}")

# other way to select a random friend.
random_index = random.randint(0,3)
print(friends[random_index])

# using len() :
random.randint(0, len(friends) - 1)  # Generates a random index based on the length of the list.
print(f"Randomly selected friend using len: {friends[random.randint(0, len(friends) - 1)]}")

# Nested Lists :
fruit_basket = ["Apple", "Banana", "Cherry"]
vegetable_basket = ["Carrot", "Broccoli", "Spinach"]
grocery_basket = [fruit_basket, vegetable_basket]  # Creating a nested list.
print(grocery_basket)
# Accessing elements in a nested list.
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
dirty_dozen = [fruits, vegetables]
 
print(dirty_dozen[1][1])

# useful stuff :
# is.digit() checks if the input is a digit.it is string function.
# If the input is a digit, it will return True, otherwise False.
# then it converts the input to an integer.
# exit() is used to terminate the program.