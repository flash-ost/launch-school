"""
Convert a Number to a String
In the previous two exercises, you developed functions that convert simple numeric strings to signed integers. In this exercise and the next, you're going to reverse those functions.

Write a function that converts a non-negative integer value (e.g., 0, 1, 2, 3, and so on) to the string representation of that integer.

You may not use any of the standard conversion functions available in Python, such as str. Your function should do this the old-fashioned way and construct the string by analyzing and manipulating the number.

Examples
print(integer_to_string(4321) == "4321")              # True
print(integer_to_string(0) == "0")                    # True
print(integer_to_string(5000) == "5000")              # True
print(integer_to_string(1234567890) == "1234567890")  # True
"""

## Understanding
# Input: non-negative int
# Output: inputted int as string
# Explicit rules:
# - conversion functions are prohibited
# - only non-negative ints as input

## Test Cases
# Confirm rules

## Data structure
# String to store 10 digits as chars

## Algorithm
# Create string with 10 digits from 0 to 9
# Create empty string for chars
# While loop with no condition:
#   Separate last digit by calculating remainder of dividing number by 10
#   Get corresponding char from dict and add to beginning of string
#   Divide num by 10 (integer division) and reassign its var
#   If num equals 0, break
# Return string

def integer_to_string(number):
    # Initial solution
    # CHARS = '0123456789'

    # string = ''
    # while True:
    #     string = CHARS[number % 10] + string
    #     number //= 10
    #     if number == 0:
    #         break
    # return string   

    # Using divmod function
    CHARS = '0123456789'

    string = ''
    while number > 0:
        number, remainder = divmod(number, 10)
        string = CHARS[remainder] + string
    return string or '0'

print(integer_to_string(4321) == "4321")              # True
print(integer_to_string(0) == "0")                    # True
print(integer_to_string(5000) == "5000")              # True
print(integer_to_string(1234567890) == "1234567890")  # True