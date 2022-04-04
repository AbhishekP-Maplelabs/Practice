"""
module:1
description:to convert 12 hour format to 24 hour format
"""
def convert24(str1):
	if str1[-2:] == "AM" and str1[:2] == "12":
		return "00" + str1[2:-2]
	elif str1[-2:] == "AM":
		return str1[:-2]
	elif str1[-2:] == "PM" and str1[:2] == "12":
		return str1[:-2]		
	else:		
		return str(int(str1[:2]) + 12) + str1[2:8]
Time=input("Enter the time: ")
if Time[0:3] and Time[5:7] and Time[7:9].isnumeric():
    NewTime=convert24(Time)
else:
    print("please enter the proper time formet")
    exit()
print(f"The time in 12 hour format is :{Time}")
print(f"Time in 24 hour format is: {NewTime}")

