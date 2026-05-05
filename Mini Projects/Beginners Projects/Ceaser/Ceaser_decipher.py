import os
import art

print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceaser_decipher(direction, text, shift):
    cipher=""
    if direction == "decode":
        shift *= -1

    for letter in text:
        if letter not in alphabet:
            cipher += letter
        else:
            a = (alphabet.index(letter) + shift) % len(alphabet)
            cipher += alphabet[a]
    print(f"The {direction}d text is {cipher}")

def brute_force(text):
    print(art.HACKER_ART)
    print("*/*/*/*Hacker Mode Activated*/*/*/*\n")
    print("Trying all possible shifts:\n")

    for shift in range(1, 27):
        deciphered_text = ""
        for letter in text:
            if letter not in alphabet:
                deciphered_text += letter
            else:
                a = (alphabet.index(letter) - shift) % len(alphabet)
                deciphered_text += alphabet[a]
        print(f"Shift {shift}: {deciphered_text}\n")
    print("*/*/*/*End of Hacker Mode*/*/*/*\n")

isCeaser = True
while isCeaser:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt, or type 'brute force' to try all shifts:\n").lower()
    while direction not in ["encode", "decode", "brute force"]:
        print("Invalid input. Please Check your spelling and try again.\n")
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt, or type 'brute force' to try all shifts:\n").lower()
        print("=====================================================================================\n")

    text = input("Type your message:\n").lower()
    print("=====================================================================================\n")
    if direction == "brute force":
        brute_force(text)
    else:    
        while True:
            try:
                shift = int(input("Type the shift number:\n"))
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer for the shift number.\n")
                ceaser_decipher(direction, text, shift)
    print("=====================================================================================\n")

    

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    while restart not in ["yes", "no"]:
        print("Invalid input. Please Check your spelling and try again.\n")
        restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
        print("=====================================================================================\n")

    if restart == "no":
        isCeaser = False
        print("Goodbye!")      
    else:
        os.system('cls' if os.name == 'nt' else 'clear')            