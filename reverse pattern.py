rows = int(input("Enter number of rows:"))
c = 0
# reverse for loop from 5 to 0
for i in range(rows, 0, -1):
    c = c + 1
    for j in range(1, 1+i):
        print(j,end="")
    print("\r")
