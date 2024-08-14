"""
List Average
Write a function that takes one argument, a list of integers, and returns the average of all the integers in the list, rounded down to the integer component of the average. The list will never be empty, and the numbers will always be positive integers.

Examples
print(average([1, 5, 87, 45, 8, 8]) == 25)        # True
print(average([9, 47, 23, 95, 16, 52]) == 40)     # True
print(average([7]) == 7)                          # True
"""

## Understanding
# Input: list of integers
# Output: averae of all ints in list, rounded to integer component

# Explicit rules
#  - list will never be empty
#  - all elements will always be positive ints

## Test cases
# No new info

# Data structure
# No

## Algorithm
# Add all elements of list, divide sum by num of elements (integer division)
# Return result

def average(list):
    return sum(list) // len(list)

print(average([1, 5, 87, 45, 8, 8]) == 25)        # True
print(average([9, 47, 23, 95, 16, 52]) == 40)     # True
print(average([7]) == 7)    