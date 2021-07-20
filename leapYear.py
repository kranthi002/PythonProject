# Leap year program using function:
def leapyr(n):
    if n % 400 == 0:
        return True
    if n % 100 == 0:
        return False
    if n % 4 == 0:
        return True
    return False
print (leapyr(int(input("Enter the year:"))))

# Leap year program using built in function:
import calendar
print(calendar.isleap(int(input("Enter the year:"))))