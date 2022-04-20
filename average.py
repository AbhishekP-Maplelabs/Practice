"""
module:2
description:To find the average of the numbers entered
"""
def average(add,number):
    """
    To find the average of the numbers
    """
    avg=add//number
    return avg
List = []
ADD_NUM=0
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input())
    List.append(ele)
print(List)
for i in range(0,len(List)):
    ADD_NUM=ADD_NUM+List[i]
print(ADD_NUM)
result=average(ADD_NUM,n)
print(result)
