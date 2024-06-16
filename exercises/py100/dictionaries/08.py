"""
Which Collection?
Rewrite car as a nested list containing the same key/value pairs.

car = {
    'type':  'sedan',
    'color': 'blue',
    'year':  2003,
}
"""

car = {
    'type':  'sedan',
    'color': 'blue',
    'year':  2003,
}

lst = [[key, car[key]] for key in car]
lst2 = [[key, value] for key, value in car.items()]
print(lst)
print(lst2)