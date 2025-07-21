# This is my Treasure Island game code:
print("Welcome to the Treasure Island!")
print("Your mission is to find the treasure.")
choice1 = input('You\'re at a crossroad. Where do you want to go? \n Type "Left" or "Right".').lower()
# Continue the game based on the user's choice.
if choice1 == "left":
    choice2 = input("You\'ve come to a lake. There is an island in the middle of the lake. \n Type 'Swim' to swim across or 'Wait' to wait for a boat :").lower()
    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed.\n There is a house with 3 doors.\n One red, one yellow and one blue.\n Which color do you choose?").lower()
        if choice3 == "red":
            print("It's a room full of fire. Game Over.")
        elif choice3 == "yellow":
            print("You found the treasure! You Win!")
        elif choice3 == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else :    
        print("You swam across and were attacked by a trout. Game Over.")
else :    
    print("You fell into a hole. Game Over.")
print("Thank you for playing Treasure Island!")

