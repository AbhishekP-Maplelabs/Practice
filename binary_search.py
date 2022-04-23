"""
module:Practice
description:To search the element using binary search algorithm
"""
def binary_search(array_1, key_num, low, high):
    """
    Find the key element using binary search algorithm
    """
    while low <= high:
        mid = low + (high - low)//2
        if array_1[mid] == key_num:
            return mid
        elif array_1[mid] < key_num:
            low = mid + 1
        else:
            high = mid - 1
    return -1
try:
    NUM=int(input("Enter the size of the array: "))
    array=[]
    for i in range(NUM):
        ELEMENT=int(input())
        array.append(ELEMENT)
    key=int(input("Enter the key number to search"))
    RESULT = binary_search(array, key, 0, len(array)-1)
    if RESULT != -1:
        print(f"Element is present at index {RESULT}")
    else:
        print("key Not found")
except Exception as e:
    print("Run again and enter the valid input")
