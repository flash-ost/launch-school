"""
Triangle Sides
A triangle is classified as follows:

Equilateral: All three sides have the same length.
Isosceles: Two sides have the same length, while the third is different.
Scalene: All three sides have different lengths.
To be a valid triangle, the sum of the lengths of the two shortest sides must be greater than the length of the longest side, and every side must have a length greater than 0. If either of these conditions is not satisfied, the triangle is invalid.

Write a function that takes the lengths of the three sides of a triangle as arguments and returns one of the following four strings representing the triangle's classification: 'equilateral', 'isosceles', 'scalene', or 'invalid'.

Examples
print(triangle(3, 3, 3) == "equilateral")  # True
print(triangle(3, 3, 1.5) == "isosceles")  # True
print(triangle(3, 4, 5) == "scalene")      # True
print(triangle(0, 3, 3) == "invalid")      # True
print(triangle(3, 1, 1) == "invalid")      # True
"""

## Understanding
# Input: 3 numbers representing lengths of triangle sides
# Output: string characterizing the triangle
#   - 'equilateral' if all sides are equal
#   - 'isosceles' if 2 sides are equal
#   - 'scalene' if all sides have different length
#   - 'invalid' if either of 2 conditions is not satisfied: 
#       lengths of the two shortest sides must be greater than the length of the longest side
#       every side must have a length greater than 0

## Algorithm
# Store input numbers in a list called sides
# If 0 is in sides:
#   return 'invalid'
# If sum of 2 first elements of sorted list is less than the third element:
#   return 'invalid'

# Convert list to set
# If length of set is 1:
#   return 'equilateral'
# elif length of set is 2:
#   return 'isosceles'
# else
#   return 'scalene'

def triangle(a, b, c):
    sides = [a, b, c]
    sides.sort()
    if 0 in sides or sum(sides[:2]) < sides[2]:
        return 'invalid'
    
    unique = len(set(sides))
    match unique:
        case 1:
            return 'equilateral'
        case 2:
            return 'isosceles'
        case 3:
            return 'scalene'

print(triangle(3, 3, 3) == "equilateral")  # True
print(triangle(3, 3, 1.5) == "isosceles")  # True
print(triangle(3, 4, 5) == "scalene")      # True
print(triangle(0, 3, 3) == "invalid")      # True
print(triangle(3, 1, 1) == "invalid")      # True