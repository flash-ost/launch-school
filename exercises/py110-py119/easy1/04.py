"""
Running Totals
Write a function that takes a list of numbers and returns a list with the same number of elements, but with each element's value being the running total from the original list.

Examples
print(running_total([2, 5, 13]) == [2, 7, 20])    # True
print(running_total([14, 11, 7, 15, 20])
      == [14, 25, 32, 47, 67])                    # True
print(running_total([3]) == [3])                  # True
print(running_total([]) == [])                    # True
"""

## Understanding
# Input: list of numbers
# Output: list with the same number of elements, but each element's value is a running total from original list
# Questions: What exactly is meant by running total?

## Test Cases
# Running total is current el + all previous
# If input is list with 1 el or empty list, return the same list

## Data Structure
# List

## Algorithm
# Create new empty list
# Create var for holding running total
# Iterate over elements of original list
#   - add current el to total
#   - append total to new list
# Return new list

def running_total(numbers):
    new_list = []
    total = 0

    for num in numbers:
        total += num
        new_list.append(total)
    return new_list        

print(running_total([2, 5, 13]) == [2, 7, 20])    # True
print(running_total([14, 11, 7, 15, 20])
      == [14, 25, 32, 47, 67])                    # True
print(running_total([3]) == [3])                  # True
print(running_total([]) == [])                    # True