"""
module:math
description:finding the maximum of two numbers
"""
def maximum(num1,num2):
    """
   To find the maximum among the two numbers
    """
    if(num1>num2):
        return num1
    else:
        return num2
    

num1=int(input("Enter the first number"))
num2=int(input("Enter the second number"))
result=maximum(num1,num2)
print(result,"is the maximum number")