"""
Immutable Intersection
Transform two lists into frozen sets and find their common elements.

Example
list1 = [2, 4, 6, 8]
list2 = [1, 3, 5, 7, 8]
expected_result = frozenset({8})
print(intersection(list1, list2) == expected_result) # True
"""

## Understanding
# Input: 2 lists
# Output: intersection of frozen sets created from input lists

## Data Structure
# Frozen Set

## Algorithm
# Convert input lists into frozen sets
# Return intersection of frozen sets

def intersection(list1, list2):
    return frozenset(list1) & frozenset(list2)

list1 = [2, 4, 6, 8]
list2 = [1, 3, 5, 7, 8]
expected_result = frozenset({8})
print(intersection(list1, list2) == expected_result) # True