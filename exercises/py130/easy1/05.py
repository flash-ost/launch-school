"""
Remove None Values
Remove all None values from a list using the filter method.
"""
lst = [True, None, '23', 25, False, None]
print(list(filter(lambda x: x != None, lst)))