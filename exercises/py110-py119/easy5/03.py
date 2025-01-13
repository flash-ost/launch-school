"""
Write a function that takes a list of strings and returns a list of the same string values, but with all vowels (a, e, i, o, u) removed.

Examples
# All of these examples should print True
original = ['abcdefghijklmnopqrstuvwxyz']
expected = ['bcdfghjklmnpqrstvwxyz']
print(remove_vowels(original) == expected)        # True

original = ['green', 'YELLOW', 'black', 'white']
expected = ['grn', 'YLLW', 'blck', 'wht']
print(remove_vowels(original) == expected)        # True

original = ['ABC', 'AEIOU', 'XYZ']
expected = ['BC', '', 'XYZ']
print(remove_vowels(original) == expected)        # True
"""

## Understanding
# Input: list of strings
# Output: list of strings, but with all vowels removed

# Implicit rules
# - if original string contained only vowels, output string should be empty
# - both upper- and lowercase vowels should be removed

## Data Structure
# List

## Algorithm
# Create VOWELS string consisting of lowercase vowels (lowercase + uppercase)
# Create empty list for new strings
# Iterate over strings in list:
#   Initialize new empty string
#   Iterate over letters in string from list:
#       if it's not a vowel:
#           add to new string
#   Add new string to new list
# return new list
VOWELS = 'aeiouAEIOU'

def is_vowel(char):
    return True if char in VOWELS else False

def remove_vowels(lst):
    return [''.join([letter for letter in string if not is_vowel(letter)]) for string in lst]

original = ['abcdefghijklmnopqrstuvwxyz']
expected = ['bcdfghjklmnpqrstvwxyz']
print(remove_vowels(original) == expected)        # True

original = ['green', 'YELLOW', 'black', 'white']
expected = ['grn', 'YLLW', 'blck', 'wht']
print(remove_vowels(original) == expected)        # True

original = ['ABC', 'AEIOU', 'XYZ']
expected = ['BC', '', 'XYZ']
print(remove_vowels(original) == expected)        # True