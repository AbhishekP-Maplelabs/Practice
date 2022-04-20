"""
module:2
description:Finding the second largset number
"""
import array as arr
def bubble_sort(array_1):
    """
        To find the second largest number
    """
    for k in range(n-1):
        for j in range(0, n-k-1):
            if array_1[j] > array_1[j + 1]:
                array_1[j], array_1[j + 1] = array_1[j + 1],array_1[j]
arr = []
n = int(input("Enter the array size"))
for i in range (0,n):
    numbers=int(input())
    arr.append(numbers)
bubble_sort(arr)
print ("Sorted array is:")
for i in range(len(arr)):
    print ("% d" % arr[i],end=" ")
print()
print(f"The second largest nymber is: {arr[1]}")
