"""
module:math
description:finding wheather the given number is even or odd
"""
def evenorodd(a):
    """
    Checks whether the number is even or odd
    """
    b=a%2
    return b

if __name__ == "__main__":   
 a=int(input("Enter a number"))
num=evenorodd(a)
if(num==0):
    print(a,"is even number")
else:
    print(a,"is odd number")