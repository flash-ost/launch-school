"""
Last Element
Write a function that returns the last element of a list provided as an argument. For example:

print(last(['Earth', 'Moon', 'Mars']))  # Mars
Be sure to handle the case where the input list is empty.
"""
def last(lst):
    # return lst[len(lst) - 1] if lst else None
    return lst[-1] if lst else None

print(last(['Earth', 'Moon', 'Mars']))  # Mars
print(last([]))
