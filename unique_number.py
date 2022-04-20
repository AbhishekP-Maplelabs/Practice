"""
module:2
description:to check wheather the numbers are unique or not
"""
import array as arr
arr = []
n = int(input("Enter the array size: "))
for i in range (0,n):
    numbers=int(input())
    arr.append(numbers)
print(arr)
for k in range(n-1):
    for j in range(0, n-k-1):
        if arr[j] == arr[j + 1]:
            print("false")
            quit()
        else:
            print("true")
            quit()
