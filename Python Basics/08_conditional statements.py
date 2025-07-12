# Conditional Statements in Python.
#  If and else statements.
# Example 1: Basic if-else statement.
print("Welcome to the Roller Coaster!")
height= int(input("Please enter your height in cm: "))

if height >= 120:
    print("You can ride the roller coaster!")
else:
    print("Sorry, you are not tall enough to ride the roller coaster.")

# Modulo Operator.
print(10 % 3) 

# Example 2: Using modulo operator to check even or odd.
number_to_check =int(input("Enter a number to check if it's even or odd: "))
if number_to_check % 2 == 0 :
    print(f"{number_to_check} is an even number.")
else:
    print(f"{number_to_check} is an odd number.")