"""
Alphabetical Numbers
Write a function that takes a list of integers between 0 and 19 and returns a list of those integers sorted based on the English word for each number:

zero, one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen

Example
input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
              10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

expected_result = [8, 18, 11, 15, 5, 4, 14, 9, 19, 1,
                   7, 17, 6, 16, 10, 13, 3, 12, 2, 0]

print(alphabetic_number_sort(input_list) == expected_result)
# Prints True
"""

## Understanding
# Input: list of integers between 0 and 19
# Output: list of those integers sorted based on the English word for each number

## Testing
# No duplicate integers in input

## Data Structure
# List

## Algorithm
# Zip integers with corresponding English words
# Unpack pairs into list
# Sort the list lexicographically
# Create a final list, taking second elements of each pair in sorted list
# Return the list of sorted integers

def alphabetic_number_sort(list):
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
    'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen',
    'seventeen', 'eighteen', 'nineteen']
    return [el[1] for el in sorted([el for el in zip(words, input_list)])]


input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
              10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

expected_result = [8, 18, 11, 15, 5, 4, 14, 9, 19, 1,
                   7, 17, 6, 16, 10, 13, 3, 12, 2, 0]

print(alphabetic_number_sort(input_list) == expected_result)

## Solution 2
# words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
#     'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen',
#     'seventeen', 'eighteen', 'nineteen']

# def word_for_number(num):
#     return words[num]

# def alphabetic_number_sort(numbers):
#     return sorted(numbers, key=words)