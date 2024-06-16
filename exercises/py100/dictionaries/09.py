"""
Divided by Two
Use a for loop to iterate over the numbers dictionary and return a list containing each number divided by 2. Assign the returned list to a variable named half_numbers and print its value using print.

numbers = {
    'high':   100,
    'medium': 50,
    'low':    10,
}
Expected Output
[50, 25, 5]
"""

numbers = {
    'high':   100,
    'medium': 50,
    'low':    10,
}

half_numbers = [value // 2 for value in numbers.values()]
print(half_numbers)