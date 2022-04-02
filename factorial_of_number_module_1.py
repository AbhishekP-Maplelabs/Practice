"""
module:math
description:To find the factorial of a number
"""

def factorial(num):
    """This is a recursive function
    to find the factorial of an integer"""
    if int(num) == 0:
        return 1
    fact= int(num) * factorial(int(num)-1)
    return fact
try:
    number = input("Enter the number: ")
    result = factorial(number)
    print("The factorial of", number, "is", result)
except Exception as e:
    print ("please enter the positive integer")
