import random
from words import word_list as words
from arts import logo, stages

chosen_word = random.choice(words)
print("chosen word length is : " + str(len(chosen_word)))

print(logo)
placeholder = ""
for i in range(len(chosen_word)):
    placeholder += "_"
print(placeholder)


game_over = False
correct = []
lives = 6

while not game_over:
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()
    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct.append(letter)
        elif letter in correct:
            display += letter    
        else:
            display += "_" 
    print("Word to guess:", display)

    if guess in display:
        print(f"Good job! {guess} is in the word.")
        
    if guess in correct:
        print(f"You've already guessed {guess}")
        print("No penalty for repeated guess.")
        print(f"Lives remaining: {lives}")

    if guess not in chosen_word:
        lives -= 1
        print(f"You lost a life. Lives remaining: {lives}")
        if lives == 0:
            game_over = True
            print("You Lose!")
            print(f"The word was: {chosen_word}")

    if "_" not in display:
        game_over = True
        print("You Win!")

    print(stages[lives])    