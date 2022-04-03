"""
module:1
description:to convert snake case to pascle case
"""
from string import capwords
try:
    string=input("Enter the string: ")
    if string.isnumeric():
        print("please enter string")
        exit()
        print("Snake case: ",string)
    Pascal_Case= capwords(string.replace('_',' '))
    PascaCase= Pascal_Case.replace(' ','')
    print("Pascal case: ",Pascal_Case)
except Exception as e:
    print("Enter the valid input")