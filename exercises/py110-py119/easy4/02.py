"""
Merge Sets
Given two lists, convert them to sets and return a new set which is the union of both sets.

Example
list1 = [3, 5, 7, 9]
list2 = [5, 7, 11, 13]
print(merge_sets(list1, list2) == {3, 5, 7, 9, 11, 13})
# Prints True
"""

## Understanding
# Input: 2 lists
# Output: set which is the union of both lists converted to sets

## Data Structure
# Set

## Algorithm
# Convert both lists to sets
# Return a union of sets


def merge_sets(list1, list2):
    return set(list1) | set(list2)

list1 = [3, 5, 7, 9]
list2 = [5, 7, 11, 13]
print(merge_sets(list1, list2) == {3, 5, 7, 9, 11, 13})