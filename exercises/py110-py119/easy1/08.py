"""
Convert a String to a Number
Write a function that takes a string of digits and returns the appropriate number as an integer. You may not use any of the standard conversion functions available in Python, such as int. Your function should calculate the result by using the characters in the string.

For now, do not worry about leading + or - signs, nor should you worry about invalid characters; assume all characters are numeric.

Examples
print(string_to_integer("4321") == 4321)  # True
print(string_to_integer("570") == 570)    # True
"""

## Understanding
# Input: string of digits
# Output: integer converted from input string
# Explicit rules:
# - standard conversion functions (int) are prohibited
# - string will only contain digits

# Questions
# Is ord() function prohibited too?

## Test cases
# Don't help much

## Data structure
# Just int for storing converted number

## Algorithm
# Create a dict with char digits corresponding to numbers
# Create var for converted number, initialize to 0
# Iterate over chars in string:
#   - multiply current num by 10, add new number by accessing dict value
# Return number

# def string_to_integer(string):
#     DIGITS = {
#               '0': 0,
#               '1': 1,
#               '2': 2,
#               '3': 3,
#               '4': 4,
#               '5': 5,
#               '6': 6,
#               '7': 7,
#               '8': 8,
#               '9': 9,
#               }
    
#     number = 0
#     for char in string:
#         number = 10 * number + DIGITS[char]

#     return number    

# print(string_to_integer("4321") == 4321)  # True
# print(string_to_integer("570") == 570)    # True

"""
Further Exploration
Write a hexadecimal_to_integer function that converts a string representing a hexadecimal number to its integer value. Hexadecimal numbers use base 16 instead of 10, and the characters A, B, C, D, E and F (and the lowercase equivalents) correspond to decimal values of 10-15.

Example
print(hexadecimal_to_integer('4D9f') == 19871)  # True
"""

# What to modify
# Add A-F entries to dictionary
# Replace decimal multiplier (10) with hexadecimal (16)
# Convert letter from string to uppercase before looking up value in dictionary

def hexadecimal_to_integer(string):
    DIGITS = {
              '0': 0,
              '1': 1,
              '2': 2,
              '3': 3,
              '4': 4,
              '5': 5,
              '6': 6,
              '7': 7,
              '8': 8,
              '9': 9,
              'A': 10,
              'B': 11,
              'C': 12,
              'D': 13,
              'E': 14,
              'F': 15,
              }
    
    number = 0
    for char in string:
        number = 16 * number + DIGITS[char.upper()]

    return number    

print(hexadecimal_to_integer('4D9f') == 19871)  # True