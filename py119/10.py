"""
Problem 10
Create a function that takes a string of digits as an argument and returns the number of even-numbered substrings that can be formed. For example, in the case of '1432', the even-numbered substrings are '14', '1432', '4', '432', '32', and '2', for a total of 6 substrings.

If a substring occurs more than once, you should count each occurrence as a separate substring.

Examples
print(even_substrings('1432') == 6)
print(even_substrings('3145926') == 16)
print(even_substrings('2718281') == 16)
print(even_substrings('13579') == 0)
print(even_substrings('143232') == 12)
The above tests should each print True.
"""

# Input: string of digits
# Output: number of even-numbered substrings in the input string
# If substring occurs more than once, each occurnce should be counted separately

# Algorithm
# Initialize count to 0
# Calculate length of string
# Iterate over idx1 in range(len(string) + 1):
#   Iterate over idx2 in range(idx1 + 1, len(string) + 1):
#       if slice string[idx1:idx2] converted to int is even:
#           increment count by 1
# Return count

def even_substrings(string):
    count = 0
    length = len(string)
    for idx1 in range(length + 1):
        for idx2 in range(idx1 + 1, length + 1):
            if int(string[idx1:idx2]) % 2 == 0:
                count += 1
    return count            

print(even_substrings('1432') == 6)
print(even_substrings('3145926') == 16)
print(even_substrings('2718281') == 16)
print(even_substrings('13579') == 0)
print(even_substrings('143232') == 12)

