"""
Combine Two Lists
Write a function that combines two lists passed as arguments and returns a new list that contains all elements from both list arguments, with each element taken in alternation.

You may assume that both input lists are non-empty, and that they have the same number of elements.

Example
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
expected = [1, "a", 2, "b", 3, "c"]
print(interleave(list1, list2) == expected)      # True
"""

## Understanding
# Input: 2 lists
# Output: list with all elements of input lists, with element from each in alteration

# Explicit rules:
# Input lists will not be empty
# Input lists will have the same length

## Test Case
# Confirms rules

## Data structure:
# List

## Algorithm
# Zip elements of input lists
# Create a new list py unpacking zipped elements

def interleave(list1, list2):
    return [el for tup in zip(list1, list2) for el in tup]

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
expected = [1, "a", 2, "b", 3, "c"]
print(interleave(list1, list2) == expected)      # True