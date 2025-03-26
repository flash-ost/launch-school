"""
Write a function that rotates the last count digits of a number. To perform the rotation, move the first of the digits that you want to rotate to the end and shift the remaining digits to the left.

Examples
print(rotate_rightmost_digits(735291, 2) == 735219)  # True
print(rotate_rightmost_digits(735291, 3) == 735912)  # True
print(rotate_rightmost_digits(735291, 1) == 735291)  # True
print(rotate_rightmost_digits(735291, 4) == 732915)  # True
print(rotate_rightmost_digits(735291, 5) == 752913)  # True
print(rotate_rightmost_digits(735291, 6) == 352917)  # True
print(rotate_rightmost_digits(1200, 3) == 1002)      # True
"""

## Understanding
# Input: int
# Output: int - input number, but with N lats digits rotated. Rotation means that the first digit of given N digits goes to the end.

## Algorithm
# Convert number to a string
# Create a slice from first char to Nth char from the end excluding (first_part)
# Create a slice of the rest of chars (last_part)
# Move first char of the last_part to its back
# Concatenate last_part to first_part
# Convert string to int
# Return int

def rotate_rightmost_digits(number, count):
    number_str = str(number)
    first_part = number_str[:-count]
    last_part = number_str[-count:]
    last_part = last_part[1:] + last_part[0]
    return int(first_part + last_part)

print(rotate_rightmost_digits(735291, 2) == 735219)  # True
print(rotate_rightmost_digits(735291, 3) == 735912)  # True
print(rotate_rightmost_digits(735291, 1) == 735291)  # True
print(rotate_rightmost_digits(735291, 4) == 732915)  # True
print(rotate_rightmost_digits(735291, 5) == 752913)  # True
print(rotate_rightmost_digits(735291, 6) == 352917)  # True
print(rotate_rightmost_digits(1200, 3) == 1002)      # True    
