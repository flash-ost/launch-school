"""
Problem 19
Create a function that takes a list of integers as an argument and returns the integer that appears an odd number of times. There will always be exactly one such integer in the input list.

Examples
print(odd_fellow([4]) == 4)
print(odd_fellow([7, 99, 7, 51, 99]) == 51)
print(odd_fellow([7, 99, 7, 51, 99, 7, 51]) == 7)
print(odd_fellow([25, 10, -6, 10, 25, 10, -6, 10, -6]) == -6)
print(odd_fellow([0, 0, 0]) == 0)
The above tests should each print True.
"""

# Input: list of integers
# Output: integer that appears an odd number of times in list
# There will always be exactly one such integer in list

# Algorithm
# Iterate over nums in list:
#   if number of occurrences of this num in list is odd:
#       return num

def odd_fellow(lst):
    for num in lst:
        if lst.count(num) % 2 != 0:
            return num

print(odd_fellow([4]) == 4)
print(odd_fellow([7, 99, 7, 51, 99]) == 51)
print(odd_fellow([7, 99, 7, 51, 99, 7, 51]) == 7)
print(odd_fellow([25, 10, -6, 10, 25, 10, -6, 10, -6]) == -6)
print(odd_fellow([0, 0, 0]) == 0)