"""
Is Empty?
Write a function that checks whether a string is empty or not. For example:

print(is_empty('mars'))  # False
print(is_empty('  '))    # False
print(is_empty(''))      # True
"""

def is_empty(str):
    # return False if str else True
    return not str

print(is_empty('mars'))  # False
print(is_empty('  '))    # False
print(is_empty(''))      # True