"""
Combining Lists
Write a function that takes two lists as arguments and returns a set that contains the union of the values from the two lists. You may assume that both arguments will always be lists.

Example
print(union([1, 3, 5], [3, 6, 9]) == {1, 3, 5, 6, 9}) # True
"""

## Understanding
# Input: 2 lists
# Output: set containing union of input lists

## Test Cases
# Not much info

## Data Structures
# Set

# Algorithm
# Create a set out of 2 lists
# Return set

def union(list1, list2):
    # return set(list1) | set(list2)
    return set(list1 + list2)

print(union([1, 3, 5], [3, 6, 9]) == {1, 3, 5, 6, 9}) # True
