# This is my Treasure Island game code:
print(''' _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/''')
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

