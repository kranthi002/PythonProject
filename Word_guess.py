# Guess the word is our new game.
# Make a list of words before game starts
import random
words = ["rabbit", "lion", "tiger", "zebra", "elephant", "snake", 
        "monkey", "deer", "bear", "dog", "cat", "pig", "horse", "camel", 
        "peacock", "parrot", "eagle", "fish", "dolphin", "whale", "lizard", "python"]
guess_word = random.choice(words)
count = 0
for count in range(5):
    act_word = input("Enter the animal:")
    if act_word == guess_word:
        print("Hurry, Your guess is correct")
        break
    else:
        print("No, Wrong guess, try again")
        count = count+1
# print("Out of attempts!")
print(guess_word)
