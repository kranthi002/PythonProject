vowels = ["a", "e", "i", "o", "u"]

name = "means it will iterate through the characters in reverse order"

words = name.split()

for i in words:
    if i[0]  not in vowels:
        print(i)