"""
First Element
Write a function that returns the first element of a list provided as an argument. For example:

print(first(['Earth', 'Moon', 'Mars']))  # Earth
Be sure to handle the case where the input list is empty.
"""

def first(lst):
    return lst[0] if lst else None

print(first(['Earth', 'Moon', 'Mars']))  # Earth
print(first([]))  # Earth