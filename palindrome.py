"""
module:Practice
Description: To check if the given word is a palindrome or not
"""
def palindrome(WORD):
    """
    To find wheather the entered word is a palindrome or not
    """
    reverse= ''.join(reversed(WORD))
    if reverse==WORD:
        return True
    else:
        return False
try:
    word=input("Enter the word or number: ")
    RESULT=palindrome(word)
    if RESULT:
        print("It is a palindrome")
    else:
        print("It is not a palindrome")
except Exception as e:
    print("Run again and enter the valid input")
