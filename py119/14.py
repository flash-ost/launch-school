"""
Problem 14
Create a function that takes a single integer argument and returns the sum of all the multiples of 7 or 11 that are less than the argument. If a number is a multiple of both 7 and 11, count it just once.

For example, the multiples of 7 and 11 that are below 25 are 7, 11, 14, 21, and 22. The sum of these multiples is 75.

If the argument is negative, return 0.

Examples
print(seven_eleven(10) == 7)
print(seven_eleven(11) == 7)
print(seven_eleven(12) == 18)
print(seven_eleven(25) == 75)
print(seven_eleven(100) == 1153)
print(seven_eleven(0) == 0)
print(seven_eleven(-100) == 0)
The above tests should each print True.
"""

# Input: single integer
# Output: sum of all multiplies of 7 or 11 that are less than the argument
# If a number is a multiple of both 7 and 11, count it just once.
# If the argument is negative, return 0

# Algorithm
# If input is less than 7, return 0
# Initialize sum to 0
# Iterate over range from 7 to input excluding
#   if current num is a multiple of 7:
#       add num to sum
#   elif current num is a multiple of 11:
#       add num to sum
# return sum

def seven_eleven(num):
    if num < 7:
        return 0
    sum = 0
    for current_num in range(7, num):
        if current_num % 7 == 0:
            sum += current_num
        elif current_num % 11 == 0:
            sum += current_num

    return sum        

print(seven_eleven(10) == 7)
print(seven_eleven(11) == 7)
print(seven_eleven(12) == 18)
print(seven_eleven(25) == 75)
print(seven_eleven(100) == 1153)
print(seven_eleven(0) == 0)
print(seven_eleven(-100) == 0)
