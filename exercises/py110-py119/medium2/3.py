"""
PY110-PY119 Small ProblemsMedium 2Tri-Angles
Give us your feedback
Tri-Angles
A triangle is classified as follows:

Right: One angle is a right angle (exactly 90 degrees).
Acute: All three angles are less than 90 degrees.
Obtuse: One angle is greater than 90 degrees.
To be a valid triangle, the sum of the angles must be exactly 180 degrees, and every angle must be greater than 0. If either of these conditions is not satisfied, the triangle is invalid.

Write a function that takes the three angles of a triangle as arguments and returns one of the following four strings representing the triangle's classification: 'right', 'acute', 'obtuse', or 'invalid'.

You may assume that all angles have integer values, so you do not have to worry about floating point errors. You may also assume that the arguments are in degrees.

Examples
print(triangle(60, 70, 50) == "acute")      # True
print(triangle(30, 90, 60) == "right")      # True
print(triangle(120, 50, 10) == "obtuse")    # True
print(triangle(0, 90, 90) == "invalid")     # True
print(triangle(50, 50, 50) == "invalid")    # True
"""

## Understanding
# Input: 3 integers representing triangle angles
# Output: string characterizing the triangle based on angles:
#   - 'right': one angle is a right angle (exactly 90 degrees)
#   - 'acute': all three angles are less than 90 degrees
#   - 'obtuse': one angle is greater than 90 degrees
#   - 'invalid': triangle doesn't satisfy either of conditions:
#       1) the sum of angles is exactly 180 degrees
#       2) every angle is greater than 0

## Algorithm
# Store input values in a list called angles
# If 0 is among angles or sum of angles is not equal to 180:
#   return 'invalid'
# If one angle is 90 degrees:
#   return 'right'
# Elif all three angles are less than 90 degrees:
#   return 'acute'
# else:
#   return 'obtuse'

def triangle(a, b, c):
    angles = [a, b, c]
    if 0 in angles or sum(angles) != 180:
        return 'invalid'
    
    if 90 in angles:
        return 'right'
    elif all([a < 90 for a in angles]):
        return 'acute'
    else:
        return 'obtuse'

print(triangle(60, 70, 50) == "acute")      # True
print(triangle(30, 90, 60) == "right")      # True
print(triangle(120, 50, 10) == "obtuse")    # True
print(triangle(0, 90, 90) == "invalid")     # True
print(triangle(50, 50, 50) == "invalid")    # True
