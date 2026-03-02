import os
import random
import datetime


def create_deck():
    base_cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    deck = base_cards * 4
    random.shuffle(deck)
    return deck


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def card_deal(deck):
    return deck.pop()


def adjust_for_ace(cards_list):
    while sum(cards_list) > 21 and 11 in cards_list:
        cards_list.remove(11)
        cards_list.append(1)


def calculate_score(player_cards, dealer_cards):
    if sum(player_cards) > 21:
        return "Lose"
    elif sum(dealer_cards) > 21:
        return "Win"
    elif sum(player_cards) > sum(dealer_cards):
        return "Win"
    elif sum(player_cards) == sum(dealer_cards):
        return "Draw"
    else:
        return "Lose"


def player_details():
    name = input("Please enter your name: ")
    while not name.strip():
        print("Name cannot be empty.")
        name = input("Please enter your name: ")
    return name.strip()


def player_wallet_input():
    while True:
        try:
            wallet = float(input("Enter your initial wallet amount (max $50,000): "))
            if wallet < 0:
                print("Wallet cannot be negative.")
                continue
            if wallet > 50000:
                print("Maximum allowed is $50,000.")
                continue
            return wallet
        except ValueError:
            print("Invalid input. Enter a number.")


def dealer_wallet_input():
    while True:
        try:
            wallet = float(input("Enter dealer's wallet amount (max $50,000): "))
            if wallet < 0:
                print("Wallet cannot be negative.")
                continue
            if wallet > 50000:
                print("Maximum allowed is $50,000.")
                continue
            return wallet
        except ValueError:
            print("Invalid input. Enter a number.")


def bet_amount(player_wallet, dealer_wallet):
    while True:
        try:
            bet = float(input("Enter your bet amount: "))
            if bet <= 0:
                print("Bet must be greater than 0.")
                continue
            if bet > player_wallet:
                print("You cannot bet more than your wallet.")
                continue
            if bet > dealer_wallet:
                print("Dealer cannot cover that bet.")
                continue
            return bet
        except ValueError:
            print("Invalid input. Enter a number.")


def update_wallet(result, bet, player_wallet, dealer_wallet):
    if result == "Win":
        player_wallet += bet * 2
        dealer_wallet -= bet * 2
        print(f"You win! Wallet: ${player_wallet:.2f}")

    elif result == "Draw":
        player_wallet += bet
        dealer_wallet -= bet
        print("It's a draw! Bet returned.")

    else:
        print(f"You lose! Wallet: ${player_wallet:.2f}")

    return player_wallet, dealer_wallet


def game(player_name, player_wallet, dealer_wallet):
    clear_screen()

    player_cards = []
    dealer_cards = []
    isFirstRound = True

    print(f"\nHello {player_name}!")
    print(f"Your wallet: ${player_wallet:.2f}")
    print(f"Dealer wallet: ${dealer_wallet:.2f}")

    bet = bet_amount(player_wallet, dealer_wallet)

    player_wallet -= bet
    dealer_wallet += bet

    print(f"You bet: ${bet:.2f} | Remaining wallet: ${player_wallet:.2f}")

    deck = create_deck()

    for _ in range(2):
        player_cards.append(card_deal(deck))
        dealer_cards.append(card_deal(deck))

    print(f"Your cards: {player_cards} | Score: {sum(player_cards)}")
    print(f"Dealer's first card: {dealer_cards[0]}")

    if sum(player_cards) == 21 and len(player_cards) == 2:
        print("BLACKJACK! You win 3:2 payout!")
        player_wallet += bet * 2.5
        dealer_wallet -= bet * 2.5
        return True, player_wallet, dealer_wallet

    while sum(player_cards) < 21:
        choice = input("Type 'y' to hit, 'n' to stand, 'd' to double down: ").lower()

        if choice == 'y':
            player_cards.append(card_deal(deck))
            adjust_for_ace(player_cards)
            print(f"Your cards: {player_cards} | Score: {sum(player_cards)}")
            isFirstRound = False

        elif choice == 'n':
            break

        elif choice == 'd' and isFirstRound:
            if bet > player_wallet:
                print("You don't have enough to double down.")
                continue

            player_wallet -= bet
            dealer_wallet += bet
            bet *= 2

            player_cards.append(card_deal(deck))
            adjust_for_ace(player_cards)
            print(f"Your cards: {player_cards} | Score: {sum(player_cards)}")

            break
        else:
            print("Invalid input.")

    if sum(player_cards) > 21:
        print("You bust! Dealer wins.")
        return True, player_wallet, dealer_wallet

    while sum(dealer_cards) < 17:
        dealer_cards.append(card_deal(deck))
        adjust_for_ace(dealer_cards)

    print("\nFinal Hands:")
    print(f"Your hand: {player_cards} | Score: {sum(player_cards)}")
    print(f"Dealer hand: {dealer_cards} | Score: {sum(dealer_cards)}")

    result = calculate_score(player_cards, dealer_cards)
    player_wallet, dealer_wallet = update_wallet(result, bet, player_wallet, dealer_wallet)

    with open("blackjack_log.txt", "a") as log_file:
        log_file.write(f"Game on {datetime.datetime.now()}\n")
        log_file.write(f"Player: {player_cards} ({sum(player_cards)})\n")
        log_file.write(f"Dealer: {dealer_cards} ({sum(dealer_cards)})\n")
        log_file.write(f"Result: {result}\n")
        log_file.write("-" * 30 + "\n")

    if player_wallet <= 0:
        print("You have run out of money! Game over.")
        return False, player_wallet, dealer_wallet

    if dealer_wallet <= 0:
        print("Dealer is bankrupt! You defeated the casino!")
        return False, player_wallet, dealer_wallet

    return True, player_wallet, dealer_wallet


if __name__ == "__main__":
    clear_screen()
    print("=== BLACKJACK GAME ===")

    player_name = player_details()
    player_wallet = player_wallet_input()
    dealer_wallet = dealer_wallet_input()

    while True:
        continue_game, player_wallet, dealer_wallet = game(
            player_name, player_wallet, dealer_wallet
        )

        if not continue_game:
            break

        again = input("\nPlay again? (y/n): ").lower()
        if again != 'y':
            print("Thanks for playing!")
            break

# pending work - persistent wallet, smart dealer walet and ai dealer, and stats for now.        