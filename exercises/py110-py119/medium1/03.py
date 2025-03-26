"""
Rotation (Part 3)
Take the number 735291 and rotate it by one digit to the left, getting 352917. Next, keep the first digit fixed in place and rotate the remaining digits to get 329175. Keep the first two digits fixed in place and rotate again to get 321759. Keep the first three digits fixed in place and rotate again to get 321597. Finally, keep the first four digits fixed in place and rotate the final two digits to get 321579. The resulting number is called the maximum rotation of the original number.

Write a function that takes an integer as an argument and returns the maximum rotation of that integer. You can (and probably should) use the rotate_rightmost_digits function from the previous exercise.

Examples
print(max_rotation(735291) == 321579)          # True
print(max_rotation(3) == 3)                    # True
print(max_rotation(35) == 53)                  # True
print(max_rotation(8703529146) == 7321609845)  # True

735291
352917
329175
321759
321597


# Note that the final sequence here is `015`. The leading
# zero gets dropped, though, since we're working with
# an integer.
print(max_rotation(105) == 15)                 # True
"""

## Understanding
# Input: int
# Output: int, obtained performing max rotation of original
# Example: 735291
# 1st rotation: one digit to the left (735291 -> 352917)
# 2nd rotation: first digit fixed in place, next digit rotated to the end (352917 -> 329175)
# 3rd rotation: 2 first digits in place, 3rd rotated to the end (329175 -> 321759)
# 4th rotaion: 3 first digits in place, 4th rotated to the end (321759 -> 321579)

## Algorithm
# Convert int to string and determine its length
# Iterate over decreasing range from length to 1, keeping count:
#   int = rotate_rightmost_digits(int, count)
# return int

def rotate_rightmost_digits(number, count):
    number_str = str(number)
    first_part = number_str[:-count]
    last_part = number_str[-count:]
    last_part = last_part[1:] + last_part[0]
    return int(first_part + last_part)

def max_rotation(num):
    length = len(str(num))
    for count in range(length, 1, -1):
        num = rotate_rightmost_digits(num, count)
 
    return num

print(max_rotation(735291) == 321579)          # True
print(max_rotation(3) == 3)                    # True
print(max_rotation(35) == 53)                  # True
print(max_rotation(8703529146) == 7321609845)  # True

# Note that the final sequence here is `015`. The leading
# zero gets dropped, though, since we're working with
# an integer.
print(max_rotation(105) == 15)                 # True