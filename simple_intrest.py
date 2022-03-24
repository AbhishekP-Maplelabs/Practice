"""
module:math
description:Finding the simple intrest
"""
def simpleintrest(p,t,r):
    """
    To find the simple intrest
    """
    return (p*t*r)/100

principle=int(input("Enter the princuple amount"))
time=int(input("Enter the time in years"))
rate=int(input("Enter the rate in percentage"))
SI=simpleintrest(principle,time,rate)
print("simple intrest of ",principle,"for ",time,"years at the rate of ",rate,"is ",SI,)



