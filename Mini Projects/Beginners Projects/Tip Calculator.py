# This is my third mini project in Python.
# It calculates the tip amount based on the total bill and the percentage of the tip.   
print("Welcome to the tip Calculator!")
total_bill =float(input("Enter the total bill amount? $\n")) 
tip_percentage = int(input("Enter the tip percentage you want to give? 10 12 15:\n" ))
people = int(input("How many people to split the bill? \n"))
bill_with_tip = tip_percentage / 100 * total_bill + total_bill
print("Total bill with tip is: $" + str(bill_with_tip))
bill_per_person = bill_with_tip / people
print("Each person should pay: $" + str(round(bill_per_person, 2)))