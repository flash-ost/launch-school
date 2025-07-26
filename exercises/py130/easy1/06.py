"""
Concatenate Strings
Use reduce to concatenate a list of strings into a single string.
"""
from functools import reduce

lst = ['hi', 'hello', 'hey']
print(reduce(lambda str1, str2: str1 + str2, lst))