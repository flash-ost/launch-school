"""
Mutable Default Arguments
We want to create a function that appends a given value to a list. However, the function seems to be behaving unexpectedly:

def append_to_list(value, lst=[]):
    lst.append(value)
    return lst

print(append_to_list(1) == [1])
print(append_to_list(2) == [2])
How would you fix this code?
"""
# Default argument will be the same object for all function calls, so we append the same list each time.
# If we want to work with a separate list on each call, we should initialize it inside function body.
def append_to_list(value, lst=None):
    if not lst:
        lst = []
    lst.append(value)    
    return lst

print(append_to_list(1) == [1])
print(append_to_list(2) == [2])