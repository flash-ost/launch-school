"""
How Many?
Write a function that counts the number of occurrences of each element in a given list. Once counted, print each element alongside the number of occurrences. Consider the words case sensitive e.g. ("suv" != "SUV").

Example
vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
            'motorcycle', 'motorcycle', 'car', 'truck']

count_occurrences(vehicles)
Expected Output
# your output sequence may appear in a different sequence
car => 4
truck => 3
SUV => 1
motorcycle => 2
"""

## Understanding
# Input: list with elements
# Output: print element and number of its' occurances. Format: car => 4

# Questions
# Will there be empty lists?

## Test cases
# No new info

## Data structure
# Dictionary

## Algorithm
# Create empty dict
# Iterate over list
#   if element not in dict, create new entry, set count to 1
#   if element in list, increment count in dict by 1
# Iterate over dict and print key-value pairs in desired format

# def count_occurrences(list):
#     count = {}
#     for el in list:
#         count[el] = count.get(el, 0) + 1

#     for key in count:
#         print(f'{key} => {count[key]}')    

# vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
#             'motorcycle', 'motorcycle', 'car', 'truck']

# count_occurrences(vehicles)

"""
Further Exploration
Try to solve the problem when words are case insensitive, e.g. "suv" and "SUV" represent the same vehicle type.
"""

def count_occurrences(list):
    count = {}
    for el in list:
        count[el.casefold()] = count.get(el.casefold(), 0) + 1

    for key in count:
        print(f'{key} => {count[key]}')    

vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
            'motorcycle', 'motorcycle', 'car', 'truck', 'suv', 'CaR']

count_occurrences(vehicles)