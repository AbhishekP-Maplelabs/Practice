"""
module:Practice
Description: To check if the given word is a palindrome or not
"""
def palindrome(WORD):
    """
    To find wheather the entered word is a palindrome or not
    """
    for i in range(0,len(WORD)):
        if WORD[i]==WORD[len(WORD)-1]:
            return 1
        else:
            return 0
try:
    word=input("Enter the word or number: ")
    INPUT=list(word)
    RESULT=palindrome(INPUT)
    if RESULT==1:
        print("It is a palindrome")
    else:
        print("It is not a palindrome")
except Exception as e:
    print("Run again and enter the valid input")
