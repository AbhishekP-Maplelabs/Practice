"""
module:math
description:Finding the area of the circle
"""
def area(radius):
    """
    To find the area of the circle
     """
    pi=3.142
    return pi*radius*radius



radius=int(input("Enter the radius of the circle"))
Ar=area(radius)
print("Area of circle of radius",radius,"is",Ar,"square units")