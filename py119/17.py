"""
Problem 17
Create a function that takes a list of integers as an argument. The function should determine the minimum integer value that can be appended to the list so the sum of all the elements equal the closest prime number that is greater than the current sum of the numbers. For example, the numbers in [1, 2, 3] sum to 6. The nearest prime number greater than 6 is 7. Thus, we can add 1 to the list to sum to 7.

Notes:

The list will always contain at least 2 integers.
All values in the list must be positive (> 0).
There may be multiple occurrences of the various numbers in the list.
Examples
print(nearest_prime_sum([1, 2, 3]) == 1)        # Nearest prime to 6 is 7
print(nearest_prime_sum([5, 2]) == 4)           # Nearest prime to 7 is 11
print(nearest_prime_sum([1, 1, 1]) == 2)        # Nearest prime to 3 is 5
print(nearest_prime_sum([2, 12, 8, 4, 6]) == 5) # Nearest prime to 32 is 37

# Nearest prime to 163 is 167
print(nearest_prime_sum([50, 39, 49, 6, 17, 2]) == 4)
"""

# Input: list of integers
# Output: integer representing a number that should be added to list to create a prime number
# that is greater than the sum cof current numbers in list and closest to this sum
# All values in list will be positive
# There may be multiple occurrences of the same numbers in the list

# Algorithm
# Calculate sum of numbers in list
# Initialize num to sum of numbers in list + 1
# Repeat until find the prime number:
#   increment number by 1
# Return the evaluation of number minus sum of nums in list

# Helper prime, takes number as an argument
# If num can be divided at least on one number in range from 2 to num without remainder:
#   return False
# Return True

def prime(num):
    return all([num % divisor for divisor in range(2, num)])

def nearest_prime_sum(lst):
    list_sum = sum(lst)
    num = list_sum + 1
    while not prime(num):
        num += 1
    return num - list_sum    

print(nearest_prime_sum([1, 2, 3]) == 1)        # Nearest prime to 6 is 7
print(nearest_prime_sum([5, 2]) == 4)           # Nearest prime to 7 is 11
print(nearest_prime_sum([1, 1, 1]) == 2)        # Nearest prime to 3 is 5
print(nearest_prime_sum([2, 12, 8, 4, 6]) == 5) # Nearest prime to 32 is 37

# Nearest prime to 163 is 167
print(nearest_prime_sum([50, 39, 49, 6, 17, 2]) == 4)
