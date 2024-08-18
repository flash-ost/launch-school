"""
Counting Up
Write a function that takes an integer argument and returns a list containing all integers between 1 and the argument (inclusive), in ascending order.

You may assume that the argument will always be a positive integer.

Examples
print(sequence(5) == [1, 2, 3, 4, 5])   # True
print(sequence(3) == [1, 2, 3])         # True
print(sequence(1) == [1])               # True
"""

## Understanding
# Input: positive integer
# Output: list containing all integers between 1 and the argument (inclusive), in ascending order

## Test cases
# No new info

## Data Structure
# List

## Algorithm
# Create a range of ints from 1 to input int (including)
# Convert to list and return

def sequence(num):
    return list(range(1, num + 1))

print(sequence(5) == [1, 2, 3, 4, 5])   # True
print(sequence(3) == [1, 2, 3])         # True
print(sequence(1) == [1])               # True