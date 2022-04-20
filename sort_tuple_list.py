"""
module:2
description:To sort the tuple list by first and second element
"""
list_1=[]
first_element=int(input("Enter the number of first elements: "))
for i in range(0,first_element):
    element_1=int(input())
    list_1.append(element_1)
list_2=[]
second_element=int(input("Enter the number of second elements: "))
for i in range(0,second_element):
    element_2=input()
    list_2.append(element_2)
tup=list(zip(list_1,list_2))
print(f"The entered tuple is: {tup}")
lst = len(tup)
for i in range(0, lst):
    for j in range(0, lst-i-1):
        if tup[j][1] > tup[j + 1][1]:
            temp = tup[j]
            tup[j]= tup[j + 1]
            tup[j + 1]= temp
print(f"ascending order of tuple by second element is: {tup}")
lst = len(tup)
for i in range(0, lst):
    for j in range(0, lst-i-1):
        if tup[j][1] < tup[j + 1][1]:
            temp = tup[j]
            tup[j]= tup[j + 1]
            tup[j + 1]= temp
print(f"descending order of tuple by second element is: {tup}")
NEW_ELE = 0
new_lis_len = len(tup)
for k in range(0, new_lis_len):
    for l in range(0, new_lis_len-k-1):
        if tup[l][NEW_ELE] > tup[l + 1][NEW_ELE]:
            new_tem = tup[l]
            tup[l]= tup[l + 1]
            tup[l + 1]= new_tem
print(f"Ascending order of tuple by first element is: {tup}")
NEW_ELE = 0
new_lis_len = len(tup)
for k in range(0, new_lis_len):
    for l in range(0, new_lis_len-k-1):
        if tup[l][NEW_ELE] < tup[l + 1][NEW_ELE]:
            new_tem = tup[l]
            tup[l]= tup[l + 1]
            tup[l + 1]= new_tem
print(f"descending order of tuple by first element is: {tup}")
