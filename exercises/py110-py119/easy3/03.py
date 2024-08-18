"""
Double Char (Part 1)
Write a function that takes a string, doubles every character in the string, then returns the result as a new string.

Examples
print(repeater('Hello') == "HHeelllloo")              # True
print(repeater('Good job!') == "GGoooodd  jjoobb!!")  # True
print(repeater('') == "")                             # True
"""

## Understanding
# Input: string
# Output: string with every character from original string doubled

## Test Cases
# Empty input = empty string as return value

## Data Structure
# No in first solution, list in second

## Algorithm
# Create empty string
# Iterate over chars in original string
#   double char and add to new string
# Return new string

## Using loop
# def repeater(string):
#     new = ''
#     for char in string:
#         new += char * 2
#     return new

# Using list comprehension
def repeater(string):
    return ''.join([char * 2 for char in string])

print(repeater('Hello') == "HHeelllloo")              # True
print(repeater('Good job!') == "GGoooodd  jjoobb!!")  # True
print(repeater('') == "")                             # True