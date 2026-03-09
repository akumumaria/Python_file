# Creative addition: I added a random secret word chosen from a list so the game is different each time it is played.

import random

# List of possible secret words (all lowercase)
words = ["mosiah", "temple", "moroni", "nephi", "helaman"]
secret_word = random.choice(words)

guess_count = 0

print("Welcome to the word guessing game!\n")

# Initial hint
hint = ""
for _ in secret_word:
    hint += "_ "
print(f"Your hint is: {hint}")

guess = ""

while guess != secret_word:
    guess = input("What is your guess? ").lower()
    guess_count += 1

    # Check guess length
    if len(guess) != len(secret_word):
        print("Sorry, the guess must have the same number of letters as the secret word.\n")
        continue

    # If guess is correct
    if guess == secret_word:
        break

    # Generate hint
    hint = ""
    for i in range(len(secret_word)):
        if guess[i] == secret_word[i]:
            hint += guess[i].upper() + " "
        elif guess[i] in secret_word:
            hint += guess[i].lower() + " "
        else:
            hint += "_ "

    print(f"Your hint is: {hint}\n")

print("Congratulations! You guessed it!")
print(f"It took you {guess_count} guesses.")
