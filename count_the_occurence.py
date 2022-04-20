"""
module:2
description:count the occurence of particular element
"""
List = []
n = int(input("Enter number of elements : "))
for i in range(0,n):
    ele=input()
    List.append(ele)
print(List)
print("Enter the element of which the occurence to counted: ")
element=input()
for i in List:
    if List.count(element)==0:
        print("element not present in list")
    else:
        print(List.count(element))
        quit()
