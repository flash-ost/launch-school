"""
Problem 16
Create a function that returns the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. You may assume that the input string contains only alphanumeric characters.

Examples
print(distinct_multiples('xyz') == 0)               # (none)
print(distinct_multiples('xxyypzzr') == 3)          # x, y, z
print(distinct_multiples('xXyYpzZr') == 3)          # x, y, z
print(distinct_multiples('unununium') == 2)         # u, n
print(distinct_multiples('multiplicity') == 3)      # l, t, i
print(distinct_multiples('7657') == 1)              # 7
print(distinct_multiples('3141592653589793') == 4)  # 3, 1, 5, 9
print(distinct_multiples('2718281828459045') == 5)  # 2, 1, 8, 4, 5
"""

# Input: string containing only alphanumeric characters
# Output: number of characters that occur in string more than once
# Count should be case-insensitive

# Algorithm
# Initialize empty dict counts
# Iterate over chars in string:
#   If char.lowercase() not present in counts:
#       add it to counts and set its value to 1
#   else:
#       increment value by 1
# Create a list of dict keys value of which is greater than 1
# Return the length of list

def distinct_multiples(string):
    counts = {}
    for char in string:
        counts[char.lower()] = counts.get(char.lower(), 0) + 1
    more_than_onces = [key for key in counts if counts[key] > 1]
    return len(more_than_onces)

print(distinct_multiples('xyz') == 0)               # (none)
print(distinct_multiples('xxyypzzr') == 3)          # x, y, z
print(distinct_multiples('xXyYpzZr') == 3)          # x, y, z
print(distinct_multiples('unununium') == 2)         # u, n
print(distinct_multiples('multiplicity') == 3)      # l, t, i
print(distinct_multiples('7657') == 1)              # 7
print(distinct_multiples('3141592653589793') == 4)  # 3, 1, 5, 9
print(distinct_multiples('2718281828459045') == 5)  # 2, 1, 8, 4, 5