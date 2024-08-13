"""
Halvsies
Write a function that takes a list as an argument and returns a list that contains two elements, both of which are lists. Put the first half of the original list elements in the first element of the return value and put the second half in the second element. If the original list contains an odd number of elements, place the middle element in the first half list.

Examples
# All of these examples should print True
print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
print(halvsies([5]) == [[5], []])
print(halvsies([]) == [[], []])
"""

## Understanding
# Input: list
# Output: list that contains 2 lists

# Explicit rules: 
# 1st half of the original list should be in 1st inner list, 2nd half - in 2nd inner list
# If original list contains odd number of elements, middle element goes in 1st inner list

## Test cases
# If original list contains 1 el, it goes in 1st inner list, and 2nd inner list is empty
# If original list is empty, both inner lists should be empty

## Data structure
# List with 2 nested lists

## Algorithm
# Calculate num of elements in input list, add one (works for even/odd/zero length lists)
# Divide num of elements by 2 (integer division) to determine how many elements go in each inner list
# If result is odd, add 1 to first list
# Populate new list correspondingly
# Return new list

def halvsies(list):
    half_index = (len(list) + 1) // 2
    return [list[:half_index], list[half_index:]]

print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
print(halvsies([5]) == [[5], []])
print(halvsies([]) == [[], []])