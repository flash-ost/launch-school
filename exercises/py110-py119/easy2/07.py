"""
Multiply Lists
Write a function that takes two list arguments, each containing a list of numbers, and returns a new list that contains the product of each pair of numbers from the arguments that have the same index. You may assume that the arguments contain the same number of elements.

Example
list1 = [3, 5, 7]
list2 = [9, 10, 11]
print(multiply_list(list1, list2) == [27, 50, 77])  # True
"""

## Understanding
# Input: 2 lists containing numbers
# Output: list containing the result of multiplication of each pair of nums from original list

# Explicit rules:
#  - input lists will have the same length

## Test cases
# No new info

## Data Structure
# List

# Algorithm
# Zip input lists
# Populate new list by multiplying zipped pairs
# Return new list

def multiply_list(list1, list2):
    return [num1 * num2 for num1, num2 in zip(list1, list2)]

list1 = [3, 5, 7]
list2 = [9, 10, 11]
print(multiply_list(list1, list2) == [27, 50, 77])  # True