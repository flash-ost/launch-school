"""
List of Digits
Write a function that takes one argument, a positive integer, and returns a list of the digits in the number.

Examples
print(digit_list(12345) == [1, 2, 3, 4, 5])       # True
print(digit_list(7) == [7])                       # True
print(digit_list(375290) == [3, 7, 5, 2, 9, 0])   # True
print(digit_list(444) == [4, 4, 4])               # True
"""

## Understanding
# Input: positive integer
# Output: list of digits in input number

## Test cases
# No new info

## Data structure
# List

## Algorithm
# Convert number to string
# Create list with chars of string, simultaneously converting them to ints
# Convert list elements to ints
# Return list

def digit_list(number):
    return [int(el) for el in str(number)]

print(digit_list(12345) == [1, 2, 3, 4, 5])       # True
print(digit_list(7) == [7])                       # True
print(digit_list(375290) == [3, 7, 5, 2, 9, 0])   # True
print(digit_list(444) == [4, 4, 4])               # True