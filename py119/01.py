"""
Problem 1
Create a function that takes a list of numbers as an argument. For each number, determine how many numbers in the list are smaller than it, and place the answer in a list. Return the resulting list.

When counting numbers, only count unique values. That is, if a number occurs multiple times in the list, it should only be counted once.

Examples
print(smaller_numbers_than_current([8, 1, 2, 2, 3]) == [3, 0, 1, 1, 2])
print(smaller_numbers_than_current([7, 7, 7, 7]) == [0, 0, 0, 0])
print(smaller_numbers_than_current([6, 5, 4, 8]) == [2, 1, 0, 3])
print(smaller_numbers_than_current([1]) == [0])

my_list = [1, 4, 6, 8, 13, 2, 4, 5, 4]
result   = [0, 2, 4, 5, 6, 1, 2, 3, 2]
print(smaller_numbers_than_current(my_list) == result)
"""

# Input: list of numbers
# Output: list of numbers, each representing how many numbers ini initial list are smaller than the given number

# Only count unique values when counting smaller numbers

## Algorithm
# Create empty list smaller
# Iterate over numbers of original list:
#   create a set of input list numbers that a smaller than current number
#   calculate length of set and append it to smaller list
# return smaller list

def smaller_numbers_than_current(lst):
    smaller = []
    for number in lst:
        smaller.append(len({el for el in lst if el < number}))
    return smaller    

print(smaller_numbers_than_current([8, 1, 2, 2, 3]) == [3, 0, 1, 1, 2])
print(smaller_numbers_than_current([7, 7, 7, 7]) == [0, 0, 0, 0])
print(smaller_numbers_than_current([6, 5, 4, 8]) == [2, 1, 0, 3])
print(smaller_numbers_than_current([1]) == [0])

my_list = [1, 4, 6, 8, 13, 2, 4, 5, 4]
result   = [0, 2, 4, 5, 6, 1, 2, 3, 2]
print(smaller_numbers_than_current(my_list) == result)