"""Exercise 3: Write a function calculation() such that it can accept two variables
   and calculate the addition and subtraction of them. And also it must return both 
   addition and subtraction in a single return call"""

def calc(a, b):
    for res in a,b:
        res = a + b, a - b
        return (res)
res = calc(10, 20)
print(res) 

# or else the easy way is to return the calc a , b
def calc(a, b):
    return a+b, a-b

res = calc(40, 20)
print(res)
###############

"""Exercise 4: Create a function showEmployee() in such a way 
    that it should accept employee name, and its salary and display both. 
    If the salary is missing in the function call assign default value 9000 to salary
Given:

showEmployee("Ben", 9000)
showEmployee("Ben")"""


def showEmployee(name, salary = 9000):
    print("employee", name, "salary is ", salary)

showEmployee("ben", 6000)
showEmployee("Kranthi")


################
"""Exercise 5: Create an inner function to calculate the addition in the following way
Create an outer function that will accept two parameters, a and b
Create an inner function inside an outer function that will calculate the addition of a and b
At last, an outer function will add 5 into addition and return it"""

def outerFun(a, b):
    def innerFun(a, b):
        return a+b
    add = innerFun(a,b)
    return add + 5
result = outerFun(10, 10)
print(result)

"""Exercise 6: Write a recursive function to calculate the sum of numbers from 0 to 10
Expected Output: 55 """

def calculateSum(num):
    if num:
        return num + calculateSum(num-1)
    else:
        return 0

res = calculateSum(10)
print(res)

"""Exercise 7: Assign a different name to function and call it through the new name
Below is the function displayStudent(name, age). Assign a new name showStudent(name, age) to it and call through the new name

def displayStudent(name, age):
    print(name, age)

displayStudent("Emma", 26)
You should be able to call the same function using

showStudent(name, age)"""

def displayStudent(name, age):
    print(name, age)
#displayStudent("Kranthi", 25)

showStudent = displayStudent
showStudent("Kranthi", 25)