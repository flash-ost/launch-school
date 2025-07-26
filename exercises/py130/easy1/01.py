"""
Square Numbers
Create a list where each number from the original list is squared using the map method.
"""

lst1 = [1, 2, 3, 4]
lst2 = list(map(lambda n: n ** 2, lst1))
print(lst2)