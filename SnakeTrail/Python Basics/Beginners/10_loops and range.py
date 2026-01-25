# Loops.
# Loops are used to iterate over a sequence (like a list, tuple, or string) or to repeat a block of code multiple times.
# Types of loops in Python:
#  1. for loop: Used to iterate over a sequence.
#  2. while loop: Repeats a block of code as long as a condition is true.
fruits = ["Apple", "Banana", "Cherry"]
for fruit in fruits:
    print(fruit)

# Sum Function.
# The sum() function returns the sum of all items in an iterable (like a list or tuple).
numbers = [1, 2, 3, 4, 5]
total = sum(numbers)    
print("Total:", total)  


sum = 0
for number in numbers:
    sum += number  # Adding each number to the sum variable
print("Sum using loop:", sum)

# Max Function.
# The max() function returns the largest item in an iterable or the largest of two or more arguments.
max_value = max(numbers)
print("Max value:", max_value)

max = 0
for number in numbers:
    if number > max:
        max = number  # Updating max if the current number is greater
print("Max using loop:", max)        

# Range Function.
# The range() function generates a sequence of numbers, which is often used in for loops.
for value in range(1,6):  # Generates numbers from 1 to 5
    print(value)
# Using range with a step value.
for value in range(1, 11, 2):  # Generates odd numbers from 1 to 9
    print(value)

total = 0
for value in range(1, 101):  # Sums numbers from 1 to 100
    total += value
print("Sum of numbers from 1 to 100:", total)

# While loop :
i = 0
while i < 5 :
    print("Current value of i:", i)
    i += 1  # Incrementing i to avoid infinite loop

count = 5
while (count > 0) :
    print("Count is:", count)
    count -= 1  # Decrementing count to eventually exit the loop
else :
    print("Count has reached zero, exiting loop.")
# else block executes after the while loop statement completes normally (not interrupted by a break).

# Break and Continue Statements.
# The break statement is used to exit a loop prematurely, while the continue statement skips the current iteration and moves to the next one.        
for i in range(12):
    if i == 10 :
        break  # Exits the loop when i is 10
    print("5 X", i+1, "=", 5 * (i + 1))

# Break means exit the loop when a condition is met.
# Continue means skip the current iteration and continue with the next one.  
for i in range(12):
    if i == 10 :
        print("Skip the iteration when i is 10")
        continue  # Skips the current iteration when i is 10
    print("5 X", i, "=", 5 * i)  

# Do While Loop.
# Python does not have a built-in do-while loop, but you can simulate it using a while loop with a condition that is checked at the end.
i = 0
while True:
    print("Current value of i:", i)
    i += 1
    if i >= 25:  # Condition to exit the loop
        break  # Exits the loop when i is 5 or more     
       