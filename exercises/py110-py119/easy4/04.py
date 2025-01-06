"""
Arrange a Dictionary
Given a dictionary, return its keys sorted by the values associated with each key.

Example
my_dict = {'p': 8, 'q': 2, 'r': 6}
keys = ['q', 'r', 'p']
print(order_by_value(my_dict) == keys)  # True
"""

## Understanding
# Input: dictionary
# Output: keys sorted by associated values

## Testing
# Output data type: list

## Data Structure
# List

## Algorithm
# Get dict key-value pairs
# Sort by values
# Create a list using only keys from sorted list
# Return final list

def get_value(pair):
    return pair[1]

def order_by_value(dict):
    return [key for key, value in sorted(dict.items(), key=get_value)]

my_dict = {'p': 8, 'q': 2, 'r': 6}
keys = ['q', 'r', 'p']
print(order_by_value(my_dict) == keys)  # True