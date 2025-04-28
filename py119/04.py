"""
Problem 4
Create a function that takes a list of integers as an argument and returns a tuple of two numbers that are closest together in value. If there are multiple pairs that are equally close, return the pair that occurs first in the list.

Examples
print(closest_numbers([5, 25, 15, 11, 20]) == (15, 11))
print(closest_numbers([19, 25, 32, 4, 27, 16]) == (25, 27))
print(closest_numbers([12, 22, 7, 17]) == (12, 7))
The above tests should each print True.
"""

# Input: list of integers
# Output: tuple containing 2 integers from the list that are closest in value

# If several pairs are equally close, return pair that appears first in the list

## Algorithm
# Sort the list
# Initialize difference to positive infinity
# Iterate over idg in range from 1 to length of the list:
#   if el[i] - el[i-1] < difference:
#       reassign difference to the result of el[i] - el[i-1]
#       closest_pair = (el[i-1], el[i])
# Return closest_pair

def closest_numbers(lst):
    sorted_lst = sorted(lst)

    difference = float('inf')
    for i in range(1, len(lst)):
        if sorted_lst[i] - sorted_lst[i - 1] < difference:
            difference = sorted_lst[i] - sorted_lst[i - 1]
            closest_pair = (sorted_lst[i - 1], sorted_lst[i])
    
    if lst.index(closest_pair[0]) > lst.index(closest_pair[1]):
        closest_pair = (closest_pair[1], closest_pair[0])

    return closest_pair  

# ## Solution 2
# # Algorithm
# # Initialize smallest_diff to positive infinity
# # Iterate over idx1 in range(len(lst)):
# #   iterate over idx2 in range(idx1 + 1, len(lst)):
# #       create a list containing pair [lst[idx1], lst[idx2]]
# #       calculate current_diff between numbers in pair
# #       if current_diff is smaller than smallest_diff
# #           set smallest_diff to current_diff
# #           set closest_pair to tuple (lst[idx1], lst[idx2])
# # Return closest_pair

# def closest_numbers(lst):
#     smallest_diff = float('inf')
#     for idx1 in range(len(lst)):
#         for idx2 in range(idx1 + 1, len(lst)):
#             pair_list = sorted([lst[idx1], lst[idx2]])
#             current_diff = pair_list[1] - pair_list[0]
#             if current_diff < smallest_diff:
#                 smallest_diff = current_diff
#                 pair = (lst[idx1], lst[idx2])
#     return pair        

print(closest_numbers([5, 25, 15, 11, 20]) == (15, 11))
print(closest_numbers([19, 25, 32, 4, 27, 16]) == (25, 27))
print(closest_numbers([12, 22, 7, 17]) == (12, 7))