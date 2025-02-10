"""
Key Check
You have a function that should check whether a key exists in a dictionary and returns its value. However, it's raising an error. Why is that? How would you fix this code?

def get_key_value(my_dict, key):
    if my_dict[key]:
        return my_dict[key]
    else:
        return None

print(get_key_value({"a": 1}, "b"))
"""
# When we directly access the a dictionary value using a key, if such key doesn't exist in the dict,
# Python throws KeyError. 
# This can be handled by:
#  - using try-except blocks to capture error;
#  - using a dict.get method for retrieving value - if no such key in dict, method returns a default value

def get_key_value(my_dict, key):
    # # Try / except
    # try:
    #     return my_dict[key]
    # except KeyError:
    #     return None
    
    # dict.get
    return my_dict.get(key)

print(get_key_value({"a": 1}, "b"))