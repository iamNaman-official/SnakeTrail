import os
import time
import art
import itemslist
import random
print(art.logo)

def bid_calculator(bids):
    highest_bid = 0
    winner  = []
    for bidder in bids:
        bid_amount = bids[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount

    for bidder in bids:
        if bids[bidder] == highest_bid:
            winner.append(bidder)

    print("-------------------- Auction Result ------------------")  
    if len(winner) == 1:
        print(f"The winner is {winner[0]} with a bid of ${highest_bid:.2f}")
    else:
        print(f"It's a tie between the following bidders with a bid of ${highest_bid:.2f}:")
        for w in winner:
            print(f"- {w}")    
    print("Total bidders:",len(bids))




isAuction = True
isBiding = True
bids = {}
while isAuction:
    print("Welcome to the Blind Auction Program.")
    print("Available items for auction:")

# Initialize auction pool
    auction_pool = ""
    if not auction_pool:
        auction_pool = itemslist.items_list.copy()

    current_items = random.choice(auction_pool)
    auction_pool.remove(current_items)

    while isBiding:
        print(f"Item up for auction: {current_items}")

        while True:
            name = input("What is your name?: ")
            if name in bids:
                print(f"The name {name} already bid please enter the unique name.")
            elif name == "":
                print("Name cannot be empty. Please enter a valid name.")
            else:
                break    
             
        while True:
            try:
                bid = float(input("What is your bid?: $"))
                if bid < 0:
                    print("Bid amount cannot be negative. Please enter a valid bid.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a valid number for the bid amount.")

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
            print("Clearing the screen for the next bidder...\n")
            print("Please pass the device to the next bidder.\n")
            os.system('cls' if os.name == 'nt' else 'clear')

    while True:
        continue_auction = input("\nDo you want to auction another item? (yes/no): ").lower()
        if continue_auction in ["yes", "no"]:
            break
        print("Invalid input.")

    if continue_auction == "no":
        auction_running = False
        print("Exiting Auction House. Goodbye!")
        exit()
    else:
        if not auction_pool:
            print("\nWARNING: We have auctioned every item in the catalogue!")
            reload_choice = input("Do you want to reload the items and start over? (yes/no): ").lower()
            if reload_choice == "yes":
                auction_pool = itemslist.items_list.copy() 
                print("Catalogue reloaded! Getting next item...")
            else:
                print("Auction House closing.")
                auction_running = False
        else:
            print("Setting up next item...")
     


