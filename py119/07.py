"""
Problem 7
Create a function that takes a list of integers as an argument and returns the number of identical pairs of integers in that list. For instance, the number of identical pairs in [1, 2, 3, 2, 1] is 2: occurrences each of both 2 and 1.

If the list is empty or contains exactly one value, return 0.

If a certain number occurs more than twice, count each complete pair once. For instance, for [1, 1, 1, 1] and [2, 2, 2, 2, 2], the function should return 2. The first list contains two complete pairs while the second has an extra 2 that isn't part of the other two pairs.

Examples
print(pairs([3, 1, 4, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7]) == 3)
print(pairs([2, 7, 1, 8, 2, 8, 1, 8, 2, 8, 4]) == 4)
print(pairs([]) == 0)
print(pairs([23]) == 0)
print(pairs([997, 997]) == 1)
print(pairs([32, 32, 32]) == 1)
print(pairs([7, 7, 7, 7, 7, 7, 7]) == 3)
"""

# Input: list of integers
# Output: number of identical pairs in input list

# If list is empty or contains just 1 element, return 0
# If certain number occurs more than twice, each of its pairs should be counted once:
# On input [5, 5, 5, 5, 5] the function should return 2

# Algorithm
# If list is empty or contains just 1 element, return 0
# Create set unique_nums based on input list
# Initialize count to 0
# Iterate over numbers in unique_nums:
#   count number of occurrences of current num in input list
#   integer divide it by 2
#   add result to count
# Return count

def pairs(lst):
    if len(lst) < 2:
        return 0
    unique_nums = set(lst)
    count = 0
    for num in unique_nums:
        count += lst.count(num) // 2
    return count    

print(pairs([3, 1, 4, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7]) == 3)
print(pairs([2, 7, 1, 8, 2, 8, 1, 8, 2, 8, 4]) == 4)
print(pairs([]) == 0)
print(pairs([23]) == 0)
print(pairs([997, 997]) == 1)
print(pairs([32, 32, 32]) == 1)
print(pairs([7, 7, 7, 7, 7, 7, 7]) == 3)
