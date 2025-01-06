"""
Unique Elements
From two list arguments, determine the elements that are unique to the first list. The return value should be a set.

Example
list1 = [3, 6, 9, 12]
list2 = [6, 12, 15, 18]
print(unique_from_first(list1, list2) == {9, 3})
"""

## Understanding
# Input: 2 lists
# Output: set containing elements that are unique to first list

## Data Structure
# Set

## Algorithm
# Convert lists to sets
# Return set containing unique elements of first list

def unique_from_first(list1, list2):
    return set(list1) - set(list2)

list1 = [3, 6, 9, 12]
list2 = [6, 12, 15, 18]
print(unique_from_first(list1, list2) == {9, 3})