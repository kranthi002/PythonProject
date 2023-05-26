import random

your_turn = str(input("Enter the choice of Rock, Paper or Scissor:"))
actual_turn = random.choice(["Rock", "Paper", "Scissor"])

if your_turn == actual_turn:
    print("Hurry, you both are winners")
else:
    print("You lose")