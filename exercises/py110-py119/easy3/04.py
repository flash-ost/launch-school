"""
Double Char (Part 2)
Write a function that takes a string, doubles every consonant in the string, and returns the result as a new string. The function should not double vowels ('a','e','i','o','u'), digits, punctuation, or whitespace.

You may assume that only ASCII characters will be included in the argument.

Examples
# All of these examples should print True
print(double_consonants('String') == "SSttrrinngg")
print(double_consonants('Hello-World!') == "HHellllo-WWorrlldd!")
print(double_consonants('July 4th') == "JJullyy 4tthh")
print(double_consonants('') == "")
"""

## Understanding
# Input: string
# Output: string with every consonant doubled
# Explicit rules
#   - the function should not double vowels ('a','e','i','o','u'), digits, punctuation, or whitespace
#   - only ASCII characters will be included in the argument

# Test Cases
# Empty string as aegument = empty string as return value
# Case should be preserved ('H' -> 'HH', 'l' -> 'll')

## Data Structure
# No

## Algorithm
# Create constant with upper- and lowercase consonants
# Create empty string
# Iterate over chars in string:
#   - if char is consonant, double it and add to new string
#   - if not, add char to new string
# Return new string

CONSONANTS = 'bcdfghjklmnpqrstvwxyz'

# # Loop
# def double_consonants(string):
#     new = ''
#     for char in string:
#         if char.lower() in CONSONANTS:
#             new += char * 2
#         else:
#             new += char
#     return new     

# List comprehension and joining
def double_consonants(string):
    return ''.join([char * 2 if char.lower() in CONSONANTS else char for char in string])         



# All of these examples should print True
print(double_consonants('String') == "SSttrrinngg")
print(double_consonants('Hello-World!') == "HHellllo-WWorrlldd!")
print(double_consonants('July 4th') == "JJullyy 4tthh")
print(double_consonants('') == "")