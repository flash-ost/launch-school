"""
Product of Numbers
Calculate the product of all numbers in a list using the reduce function.
"""

from functools import reduce

lst = [1, 2, 3]
print(reduce(lambda x, y: x * y, lst))