"""
Problem 20
Create a function that takes a list of numbers, all of which are the same except one. Find and return the number in the list that differs from all the rest.

The list will always contain at least 3 numbers, and there will always be exactly one number that is different.

Examples
print(what_is_different([0, 1, 0]) == 1)
print(what_is_different([7, 7, 7, 7.7, 7]) == 7.7)
print(what_is_different([1, 1, 1, 1, 1, 1, 1, 11, 1, 1, 1, 1]) == 11)
print(what_is_different([3, 4, 4, 4]) == 3)
print(what_is_different([4, 4, 4, 3]) == 3)
The above tests should each print True.
"""

# Input: list of numbers
# Output: number that appears in list exactly once
# There will always be at least 3 numbers in list

# Algorithm
# Convert input list to set
# Convert resulting set back to list
# If number of occurences of first element of new list in input list is 1:
#   return first element of new list
# else:
#   return second elemend of new list

def what_is_different(lst):
    uniques = list(set(lst))
    return uniques[0] if lst.count(uniques[0]) == 1 else uniques[1]


print(what_is_different([0, 1, 0]) == 1)
print(what_is_different([7, 7, 7, 7.7, 7]) == 7.7)
print(what_is_different([1, 1, 1, 1, 1, 1, 1, 11, 1, 1, 1, 1]) == 11)
print(what_is_different([3, 4, 4, 4]) == 3)
print(what_is_different([4, 4, 4, 3]) == 3)