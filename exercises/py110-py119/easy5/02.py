"""
Retain Specific Keys
Given a dictionary and a list of keys, produce a new dictionary that only contains the key/value pairs for the specified keys.

Example
input_dict = {
    'red': 1,
    'green': 2,
    'blue': 3,
    'yellow': 4,
}

keys = ['red', 'blue']
expected_dict = {'red': 1, 'blue': 3}
print(keep_keys(input_dict, keys) == expected_dict) # True
"""

def keep_keys(my_dict, keys_list):
    return { key: value for key, value in my_dict.items() if key in keys_list }

input_dict = {
    'red': 1,
    'green': 2,
    'blue': 3,
    'yellow': 4,
}

keys = ['red', 'blue']
expected_dict = {'red': 1, 'blue': 3}
print(keep_keys(input_dict, keys) == expected_dict) # True