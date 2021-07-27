import random

file = open("madlib.txt", "r")
madlibText = file.readlines()

madlib = random.choice(madlibText)

noun = input("Enter a noun: ")
madlib = madlib.replace("blank", noun)

print(madlib)