"""
Even Numbers
Obtain only the even numbers from a list using the filter function.
"""

lst = [1, 2, 3, 4, 5]
even_nums = list(filter(lambda x: x % 2 == 0, lst))
print(even_nums)