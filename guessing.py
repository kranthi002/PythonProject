import random
import sys
    
act_num = random.randint(1,10)
count = 0
while count<5:
    guess_num = 0
    try:
        guess_num = int(input("Enter the guessing number between 1 to 10: "))
        count += 1
        if 1 <= guess_num <= 10:
            if act_num == guess_num:
                print("Hurry, It is correct guess")
            # sys.exit
                break
            elif act_num < guess_num:
                print("No, Your guess is less than the value")
                
            elif act_num > guess_num:
                print("No, Your guess is more than the value")
        else:
            print("Out of range, please enter the number between 1 to 10")
    except:
        print("Enter a valid number")

if count==5:
    print("Out of attempts")
    print("Actual number is:",act_num)
