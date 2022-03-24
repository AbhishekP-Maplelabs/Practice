"""
module:math
description:Finding the perimeter of the circle
"""
def perimeter(radius):
    """
    To find the perimeter of the circle of given radius
    """
    pi=3.142
    return 2*pi*radius


radius=int(input("Enter the radius of the circle"))
P=perimeter(radius)
print("The perimetger of the circle of radius",radius,"is",P,"units")

