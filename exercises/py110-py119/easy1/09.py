"""
Convert a String to a Signed Number
In the previous exercise, you developed a function that converts simple numeric strings to integers. In this exercise, you're going to extend that function to work with signed numbers.

Write a function that takes a string of digits and returns the appropriate number as an integer. The string may have a leading + or - sign; if the first character is a +, your function should return a positive number; if it is a -, your function should return a negative number. If there is no sign, return a positive number.

You may assume the string will always contain a valid number.

You may not use any of the standard conversion functions available in Python, such as int. You may, however, use the string_to_integer function from the previous exercise.

Examples
print(string_to_signed_integer("4321") == 4321)  # True
print(string_to_signed_integer("-570") == -570)  # True
print(string_to_signed_integer("+100") == 100)   # True
"""

## Understanding
# Input: string of digits with or without leading + or - sign
# Output: signed integer converted from input string
# Explicit rules:
# - standard conversion functions (int) are prohibited
# - string will only contain digits and possibly leading + or - sign
# - if string has + or no leading sign, return positive int
# - if leading sign is -, return negative int

## Test cases
# Confirm explicit rules

## Data structure
# Just int for storing converted number

## Algorithm
# Create a dict with char digits corresponding to numbers
# Create a sign var and initialize to '+'
# Remove sign from string and change sign var if sign is '-'
# Create var for converted number, initialize to 0
# Iterate over chars in string:
#   - multiply current num by 10, add new number by accessing dict value

# Return positive number if sign is '+' else negative number

def string_to_signed_integer(string):
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
              }
    
    sign = '+'
    number = 0
    if string[0] in '+-':
        if string[0] == '-':
            sign = '-'
        string = string[1:]   
         
    for char in string:
        number = 10 * number + DIGITS[char]

    return number if sign == '+' else -number

print(string_to_signed_integer("4321") == 4321)  # True
print(string_to_signed_integer("-570") == -570)  # True
print(string_to_signed_integer("+100") == 100)   # True