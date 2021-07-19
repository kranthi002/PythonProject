# First import lru_cache from functools
"""
from functools import lru_cache

@lru_cache(maxsize = 100)
def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n > 2:
        return(fib(n-1) + fib(n-2))

for n in range(1, 11):
    print(n, ":", fib(n))
"""
# simple while loop:
lim = 10
a,b = 0,1
count = 0
print("Fibonacci series: ")
while count < lim:
    print(a, end = " ")
    temp = a + b

    a = b
    b = temp
    count += 1