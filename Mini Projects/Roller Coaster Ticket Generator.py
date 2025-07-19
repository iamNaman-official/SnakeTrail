# This is my Roller Coaster Ticket Price Generator.
print("Welcome to the Roller Coaster Ticket Price Generator!")
print("Please answer the following questions to determine your ticket price ?.")

height = int(input("What is your height in cm ?"))
bill = 0
# The height is checked to see if the user is tall enough to ride the roller coaster.
if height >= 120 :
    print("You can ride the roller coaster!")
    age = int(input("What is your age ?"))
    if age <= 12 :
        bill = 5
        print("Childeren's ticket price is $5.")
    elif age >12 and age < 18 :
        bill = 10
        print("Teenager's ticket price is $10.")
    else :
        bill =15
        print("Adult's ticket price is $12.") 

    print("If you want a photo taken, it will cost an extra $3.") 
    wants_photo = input("Do you want a photo taken? (yes/no) ")
    if wants_photo == "yes" :
        bill += 3
    print(f"Your total bill is $ {bill}.")    
    print("Enjoy your ride!")
else :
    print("Sorry, you are not tall enough to ride the roller coaster.")    
# This code is a simple roller coaster ticket price generator that determines the ticket price based on height and age.
# It checks if the user is tall enough to ride, then calculates the price based on age and whether they want a photo taken.    