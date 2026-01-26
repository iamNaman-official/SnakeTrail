import os
import art
print(art.logo)

def bid_calculator(bids):
    highest_bid = 0
    winner  = ""
    for bidder in bids:
        bid_amount = bids[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}.")

isAuction = True
bids = {}
while isAuction:
    print("Welcome to the Blind Auction Program.")
    name = input("What is your name?: ")
    bid = float(input("What is your bid?: $"))
    bids[name] = bid

    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    while more_bidders not in ["yes", "no"]:
        print("Invalid input. Please Check your spelling and try again.\n")
        more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
        print("=====================================================================================\n")

    if more_bidders == "no":
        isAuction = False
        bid_calculator(bids)
    else:
        os.system('cls' if os.name == 'nt' else 'clear')    