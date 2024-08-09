"""
Palindromic Strings (Part 2)
Write another function that returns True if the string passed as an argument is a palindrome, or False otherwise. This time, however, your function should be case-insensitive, and should ignore all non-alphanumeric characters. If you wish, you may simplify things by calling the is_palindrome function you wrote in the previous exercise.

Examples
print(is_real_palindrome('madam') == True)           # True
print(is_real_palindrome('356653') == True)          # True
print(is_real_palindrome('356635') == False)         # True
print(is_real_palindrome('356a653') == True)         # True
print(is_real_palindrome('123ab321') == False)       # True

# case doesn't matter
print(is_real_palindrome('Madam') == True)           # True

# only alphanumerics matter
print(is_real_palindrome("Madam, I'm Adam") == True) # True
"""

## Understanding Problem
# Input: string
# Output: boolean
# Explicit rules:
# - function should check whether passed string reads the same forwards and backwards (is a palindrome)
# - check should be case-insensitive
# - all non-alphanumeric characters should be ignored

## Test Cases
# - test cases confirm that only alphanumeric characters should be considered

## Data Structure
# No particular data structure, we will use string slicing

## Algorithm
# Create empty string
# Iterate over characters in input string:
#   - if char is alphanumeric, add it to new string (as lowercase)
# Reverse the new string using slicing
# Check whether reversed string is equal to the original (with alnum only)
# Return result

def is_real_palindrome(string):
    alnum_only = ''
    for char in string:
        if char.isalnum():
            alnum_only += char.casefold()

    return alnum_only == alnum_only[::-1]        

print(is_real_palindrome('madam') == True)           # True
print(is_real_palindrome('356653') == True)          # True
print(is_real_palindrome('356635') == False)         # True
print(is_real_palindrome('356a653') == True)         # True
print(is_real_palindrome('123ab321') == False)       # True

# case doesn't matter
print(is_real_palindrome('Madam') == True)           # True

# only alphanumerics matter
print(is_real_palindrome("Madam, I'm Adam") == True) # True