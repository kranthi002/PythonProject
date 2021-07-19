# Given a number count the total number of digits in a number

n = int(input("Enter a number: "))
count = 0
while n > 0:
    n = n // 10
    count = count + 1
print("Number of digits in the number:", count)
print("")

# Write a program to display all prime numbers within a range
for num in range(25, 50+1):
    # all prime numbers are greater than 1
    # if number is less than or equal to 1, it is not prime
    if num > 1:
        for j in range(2, num):
            # check for factors
            if (num % j) == 0:
                # not a prime number so break inner loop and
                # look for next number
                break
        else:
            print(num)