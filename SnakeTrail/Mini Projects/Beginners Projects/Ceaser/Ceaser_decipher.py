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
            a = (alphabet.index(letter) + shift)
            a %= len(alphabet)
            cipher += alphabet[a]
    print(f"The {direction}d text is {cipher}")

isCeaser = True
while isCeaser:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    print("=====================================================================================\n")

    text = input("Type your message:\n").lower()
    print("=====================================================================================\n")

    shift = int(input("Type the shift number:\n"))
    print("=====================================================================================\n")

    ceaser_decipher(direction, text, shift)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if restart == "no":
        isCeaser = False
        print("Goodbye!")              