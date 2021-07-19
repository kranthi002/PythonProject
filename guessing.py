import random
act_num = random.randrange(10)
count = 0
for count in range(5):
    guess_num = int(input("Enter the guessing number: "))
    if act_num == guess_num:
        print("Hurry, It is correct guess")
        break
    elif act_num < guess_num:
        print("No, Your guess is less than the value")
        count =+ 1
    else:
        act_num > guess_num
        print("No, Your guess is more than the value")
print("Out of attempts")
print(act_num)
