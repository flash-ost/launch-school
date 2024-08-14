"""
Multiplicative Average
Write a function that takes a list of positive integers as input, multiplies all of the integers together, divides the result by the number of entries in the list, and returns the result as a string with the value rounded to three decimal places.

Examples
# All of these examples should print True
print(multiplicative_average([3, 5]) == "7.500")
print(multiplicative_average([2, 5, 8]) == "26.667")
print(multiplicative_average([2, 5]) == "5.000")
print(multiplicative_average([1, 1, 1, 1]) == "0.250")
print(multiplicative_average([2, 5, 7, 11, 13, 17]) == "28361.667")
"""

## Understanding
# Input: list of positive integers
# Output: string that contains the result of operation: 
#  - multiplying all integers together and dividing result by number of entries.
#  - result should be rounded to three decimal places
# Questions
# Can input list be empty?
# What should be the output if lis contains just 1 entry?

## Test Cases
# Only cases with 2+ elements in input list

## Data structure
# No, just simple arithmetic

## Algorithm
# Multiply all elements of list, divide by number of elements, store result in var
# Return a result as string, rounded to 3 decima places

def multiplicative_average(list):
    result = 1

    for num in list:
        result *= num

    result /= len(list)

    return f'{result:.3f}'    


print(multiplicative_average([3, 5]) == "7.500")
print(multiplicative_average([2, 5, 8]) == "26.667")
print(multiplicative_average([2, 5]) == "5.000")
print(multiplicative_average([1, 1, 1, 1]) == "0.250")
print(multiplicative_average([2, 5, 7, 11, 13, 17]) == "28361.667")