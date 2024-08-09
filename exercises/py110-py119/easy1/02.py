"""
Palindromic Strings (Part 1)
Write a function that returns True if the string passed as an argument is a palindrome, False otherwise. A palindrome reads the same forwards and backwards. For this problem, the case matters and all characters matter.

Examples
# All of these examples should print True

print(is_palindrome('madam') == True)
print(is_palindrome('356653') == True)
print(is_palindrome('356635') == False)

# case matters
print(is_palindrome('Madam') == False)

# all characters matter
print(is_palindrome("madam i'm adam") == False)
"""

## Understanding Problem
# Input: string
# Output: boolean
# Explicit rules:
# - function should check whether passed string reads the same forwards and backwards (is a palindrome)
# - case matters
# - all characters should be considered

## Test Cases
# - test cases confirm all characters matter: there are digits, spaces, apostrophe

## Data Structure
# No particular data structure, we will use string slicing

## Algorithm
# Reverse the string using slicing
# Check whether reversed string is equal to the original
# Return result

def is_palindrome(string):
    return string == string[::-1]

print(is_palindrome('madam') == True)
print(is_palindrome('356653') == True)
print(is_palindrome('356635') == False)

# case matters
print(is_palindrome('Madam') == False)

# all characters matter
print(is_palindrome("madam i'm adam") == False)    