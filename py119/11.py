"""
Problem 11
Create a function that takes a nonempty string as an argument and returns a tuple consisting of a string and an integer. If we call the string argument s, the string component of the returned tuple t, and the integer component of the tuple k, then s, t, and k must be related to each other such that s == t * k. The values of t and k should be the shortest possible substring and the largest possible repeat count that satisfies this equation.

You may assume that the string argument consists entirely of lowercase alphabetic letters.

Examples
print(repeated_substring('xyzxyzxyz') == ('xyz', 3))
print(repeated_substring('xyxy') == ('xy', 2))
print(repeated_substring('xyz') == ('xyz', 1))
print(repeated_substring('aaaaaaaa') == ('a', 8))
print(repeated_substring('superduper') == ('superduper', 1))
The above tests should each print True.
"""

# Input: non-empty string consisting entirely of lowercase letters
# Output: tuple containing string and integer. The relation between input string,
# string in tuple and integer in tuple should be s (input) == t (tuple string) * k (tuple string)
# The values of t and k should be the shortest possible substring and the largest possible repeat count that satisfies this equation.

# Algorithm
# Iterate over range of indexes in input string, starting from the 1st:
#   if char in input with current index is equal to first elemnt in input string:
#       set substring to string[:current_index]
#      set times to length of input string integer divided by current index
#   if substring * times is equal to input string:
#       return tuple with substring and times

def repeated_substring(string):
    for i in range(1, len(string) + 1):
        substring = string[:i]
        times = len(string) // i
        if substring * times == string:
            return (substring, times)

print(repeated_substring('xyzxyzxyz') == ('xyz', 3))
print(repeated_substring('xyxy') == ('xy', 2))
print(repeated_substring('xyz') == ('xyz', 1))
print(repeated_substring('aaaaaaaa') == ('a', 8))
print(repeated_substring('superduper') == ('superduper', 1))

