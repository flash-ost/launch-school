"""
Problem 2
Create a function that takes a list of integers as an argument. The function should return the minimum sum of 5 consecutive numbers in the list. If the list contains fewer than 5 elements, the function should return None.

Examples
print(minimum_sum([1, 2, 3, 4]) is None)
print(minimum_sum([1, 2, 3, 4, 5, -5]) == 9)
print(minimum_sum([1, 2, 3, 4, 5, 6]) == 15)
print(minimum_sum([55, 2, 6, 5, 1, 2, 9, 3, 5, 100]) == 16)
print(minimum_sum([-1, -5, -3, 0, -1, 2, -4]) == -10)
The above tests should each print True.
"""

# Input: list of integers
# Output: minimum sum of 5 consecutive numbers in the list

# If less than 5 elements in list, return None

## Algorithm
# return None if length of list is less than 5
# Initialize a variable min_sum to positive infinity
# Initialize start to 0 and end to 5
# while end <= length of list:
#   if sum of elements in slice from start to end is smaller than min_sum:
#       reassign min_sum to sum of elements from curent slice
#   increment start and end by 1
# return min_sum

def minimum_sum(lst):
    length = len(lst)
    if length < 5:
        return None
    
    min_sum = float('inf')
    start = 0
    end = 5
    while end <= length:
        if sum(lst[start:end]) < min_sum:
            min_sum = sum(lst[start:end])
        start += 1
        end += 1
    return min_sum        

print(minimum_sum([1, 2, 3, 4]) is None)
print(minimum_sum([1, 2, 3, 4, 5, -5]) == 9)
print(minimum_sum([1, 2, 3, 4, 5, 6]) == 15)
print(minimum_sum([55, 2, 6, 5, 1, 2, 9, 3, 5, 100]) == 16)
print(minimum_sum([-1, -5, -3, 0, -1, 2, -4]) == -10)

