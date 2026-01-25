# This is python pizza project code :
# This code is a simple pizza ordering system that allows users to select their pizza size, toppings, and calculates the total cost.

print("Welcome to the python pizza !")
print("What would you like to order ?")
bill = 0

size = input("What size pizza do you want? (s, m, l): ")
if size == "l":
    bill = 20
    print("Large pizza costs $20")
elif size == "m":
    bill = 15
    print("Medium pizza costs $15")
else :
    bill = 10
    print("Small pizza costs $10")        
peproni = input("Do you want pepperoni? (y, n): ")
if peproni == "y":
    if size == "l":
        bill += 3
        print("Large pizza with pepperoni costs an extra $3")
    else:
        bill += 2
        print("Medium or small pizza with pepperoni costs an extra $2")
extra_cheese = input("Do you want extra cheese? (y, n): ")
if extra_cheese == "y":
    bill += 1
    print("Extra cheese costs an extra $1")
delivery = input("Do you want delivery? (y, n): ")
if delivery == "y":
    bill += 5
    print("Delivery costs an extra $5")    
tip = input("Do you want to add a tip? (y, n): ")
if tip == "y":
    tip_amount = float(input("Enter the tip amount you want to give: $"))
    bill += tip_amount
    print(f"Tip added: ${tip_amount}")
print(f"Your total bill is ${bill}.")
print("Thank you for ordering pizza with us!")
# This code is a simple pizza ordering system that allows users to select their pizza size, toppings    

