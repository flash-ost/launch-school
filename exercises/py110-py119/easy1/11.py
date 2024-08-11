"""
Convert a Signed Number to a String
In the previous exercise, you developed a function that converts non-negative numbers to strings. In this exercise, you're going to extend that function by adding the ability to represent negative numbers as well.

Write a function that takes an integer and converts it to a string representation.

You may not use any of the standard conversion functions available in Python, such as str. You may, however, use integer_to_string from the previous exercise.

Examples
print(signed_integer_to_string(4321) == "+4321")  # True
print(signed_integer_to_string(-123) == "-123")   # True
print(signed_integer_to_string(0) == "0")         # True
"""

## Understanding
# Input: int
# Output: inputted int as string
# Explicit rules:
# - conversion functions are prohibited
# - any ints as input (negative/0/positive)
# Allowed to reuse function from previous exercise

## Test Cases
# Confirm rules

## Data structure
# Same as prev exercise

## Algorithm
# Reuse integer_to_string function
# Return string

def integer_to_string(number):
    CHARS = '0123456789'

    string = ''
    while number > 0:
        number, remainder = divmod(number, 10)
        string = CHARS[remainder] + string
    return string or '0'

def signed_integer_to_string(number):
    if number > 0:
        return '+' + integer_to_string(number)
    elif number < 0:
        return '-' + integer_to_string(abs(number))
    else:
        return '0'

print(signed_integer_to_string(4321) == "+4321")  # True
print(signed_integer_to_string(-123) == "-123")   # True
print(signed_integer_to_string(0) == "0")         # True