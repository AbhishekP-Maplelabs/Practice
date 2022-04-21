"""
module:1
description:To find the sum of items in the dictionary
"""
def return_sum(myDict):
    """
    finds the sum of items in the dictionary
    """
    value_list = [i for i in myDict.values()]
    return sum(value_list)
try:
    n = int(input("N="))
    myDict = dict()
    for x in range(n):
        input_dict = input("Enter key and value:").split(":")
        myDict[input_dict[0]] = int(input_dict[1])
    print(return_sum(myDict))
except Exception as e:
    print("Enter the valid input")