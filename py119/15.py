"""
Problem 15
Create a function that takes a string argument that consists entirely of numeric digits and computes the greatest product of four consecutive digits in the string. The argument will always have more than 4 digits.

Examples
print(greatest_product('23456') == 360)      # 3 * 4 * 5 * 6
print(greatest_product('3145926') == 540)    # 5 * 9 * 2 * 6
print(greatest_product('1828172') == 128)    # 1 * 8 * 2 * 8
print(greatest_product('123987654') == 3024) # 9 * 8 * 7 * 6
The above tests should each print True.
"""

# Input: string consisting entirely of numeric digits and has more than 4 digits
# Output: integer - greatest product of 4 consecutive digits

# Algorithm
# Initialize greatest to 0
# Iterate over end indexes in range(4, len(string) + 1):
#   Create a slice string[end - 4:end]
#   convert slice to list of individual digits and convert them to ints
#   calculate product of ints
#   if product of ints in current slice is greater than greatest product,
#       assign greatest to current
# return greatest

def product(lst):
    prod = 1
    for num in lst:
        prod *= num
    return prod    

def greatest_product(string):
    greatest = 0
    for i in range(4, len(string) + 1):
        current = product([int(char) for char in string[i - 4:i]])
        if current > greatest:
            greatest = current
    return greatest

print(greatest_product('23456') == 360)      # 3 * 4 * 5 * 6
print(greatest_product('3145926') == 540)    # 5 * 9 * 2 * 6
print(greatest_product('1828172') == 128)    # 1 * 8 * 2 * 8
print(greatest_product('123987654') == 3024) # 9 * 8 * 7 * 6
