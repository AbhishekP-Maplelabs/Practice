"""
module:math
description:to find whether the given nunber is prime or not
"""
def prime_num(num):
    """
    determines whether the given number is prime or not
    """
    for i in range(2,num):
        if (num % i) == 0:
            print(num,"is not a prime number")
            print(i,"times",num//i,"is",num)
    print(num,"is a prime number")
try:
    number=int(input("Emter the number"))
    if number<=1:
        print(f"{number} is not prime number")
        quit()
    prime_num(number)
except Exception as e:
    print("please enter positive integer")
