# Write a Python function that checks whether a passed string is palindrome or not.


def palindrome_str(str):
    if str==str[::-1]:
        print('string is palindrome.')
    else:
        print('string is not palindrome.')
        
str=input('enter your string:')

palindrome_str(str)


