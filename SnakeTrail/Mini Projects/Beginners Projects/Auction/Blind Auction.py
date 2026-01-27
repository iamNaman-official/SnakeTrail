import os
import art
import itemslist
import random
print(art.logo)
# add base price for items and improve wallet system and bid validation and tie breaker system and auction history log and user authentication system.
def bid_calculator(bids,current_items):
    highest_bid = 0
    winner = []
    for bidder in bids:
        bid_amount = bids[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount

    for bidder in bids:
        if bids[bidder] == highest_bid:
            winner.append(bidder)

    wallets[winner[0]] -= highest_bid
    print(f"-------------------- Auction Result: {current_items} ------------------")  
    if len(winner) == 1 and wallets[winner[0]] > 0:
        print(f"The winner is {winner[0]} with a bid of ${highest_bid:.2f} for the item {current_items}")
        print(f"{winner[0]}'s remaining wallet balance: ${wallets[winner[0]]:.2f}")

    elif wallets[winner[0]] < 0:
        print(f"The winner is {winner[0]} with a bid of ${highest_bid:.2f} for the item {current_items}")
        print(f"However, {winner[0]} does not have sufficient funds in their wallet to complete the purchase.")
            
    else:
        print(f"It's a tie between the following bidders with a bid of ${highest_bid:.2f}:")
        for w in winner:
            print(f"- {w}")    
    print("Total bidders:",len(bids))
    

auction_pool = itemslist.items_list.copy()
wallets = {}
isAuction = True

while isAuction:
    print("Welcome to the Blind Auction Program.")
    print("Available items for auction:")

    if not auction_pool:
        print("All items have been auctioned!")
        reload = input("Reload catalogue? (yes/no): ").lower()
        if reload == "yes":
            auction_pool = itemslist.items_list.copy()
        else:
            print("Goodbye!")
            break

    current_items = random.choice(auction_pool)
    auction_pool.remove(current_items)

    isBiding = True
    bids = {}

    while isBiding:
        print(f"Item up for auction: {current_items}")

        while True:
            name = input("What is your name?: ")
            print("=====================================================================================\n")
            if name in bids:
                print(f"The name {name} already bid please enter the unique name.")
            elif name == "":
                print("Name cannot be empty. Please enter a valid name.")
            else:
                if name not in wallets:
                    print(f"Welcome {name}!. We are setting up your wallet for the auction.")  
                    while True:
                        try:
                            initial_amount = float(input(f"Enter the amount to add to your wallet, {name}: $"))
                            if initial_amount < 0:
                                print("amount cannot be negative. Please enter a valid amount.")
                            else:
                                wallets[name] = initial_amount
                                print(f"Wallet created for {name} with balance: ${wallets[name]:.2f}")
                                print("=====================================================================================\n")
                                break
                        except ValueError:
                            print("Invalid input. Please enter a valid number for the amount.")
                else:
                    print(f"Welcome back {name}! Your current wallet balance is: ${wallets[name]:.2f}")
                break                

        while True:
            try:
                bid = float(input("What is your bid?: $"))
                print("=====================================================================================\n")
                if bid < 0:
                    print("Bid amount cannot be negative. Please enter a valid bid.")
                else:
                    if bid > wallets[name]:
                        print(f"Insufficient funds in wallet. Your current balance is: ${wallets[name]:.2f}")
                    else:
                        wallets[name] -= bid
                    break
            except ValueError:
                print("Invalid input. Please enter a valid number for the bid amount.")

        bids[name] = bid

        more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
        print("=====================================================================================\n")
        while more_bidders not in ["yes", "no"]:
            print("Invalid input. Please Check your spelling and try again.\n")
            more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
            print("=====================================================================================\n")

        if more_bidders == "no":
            isBiding = False
            bid_calculator(bids,current_items)
        else:
            print("Clearing the screen for the next bidder...\n")
            print("Please pass the device to the next bidder.\n")
            os.system('cls' if os.name == 'nt' else 'clear')

    while True:
        continue_auction = input("\nDo you want to auction another item? (yes/no): ").lower()
        print("=====================================================================================\n")
        if continue_auction in ["yes", "no"]:
            break
        print("Invalid input.")

    if continue_auction == "no":
        isAuction = False
        print("Exiting Auction House. Goodbye!")
        exit()


     


