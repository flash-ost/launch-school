"""
Nested Generator Expressions
Use nested generator expressions to create a flat list of numbers from a list of lists.
"""
lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
gen = (el for sublist in lst
          for el in sublist)

print(list(gen))