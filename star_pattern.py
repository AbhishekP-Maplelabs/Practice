"""
module: 1
description:star pattern program
"""
def star_pattern(num):
    StartIndex=num
    Step=-1
    if num<=0:
        print("please enter positivr number")
    else:
        for i in range(1,num+1):
            for i in range (StartIndex,i-1,Step):
                print("*",end="")
            print()
try:
    Start=int(input("Enter the number: "))
    star_pattern(Start)
except Exception as e:
    print("please enter valid input")
