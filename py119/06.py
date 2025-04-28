"""
Problem 6
Create a function that takes a string argument and returns a dict object in which the keys represent the lowercase letters in the string, and the values represent how often the corresponding letter occurs in the string.

Examples
expected = {'w': 1, 'o': 2, 'e': 3, 'b': 1, 'g': 1, 'n': 1}
print(count_letters('woebegone') == expected)

expected = {'l': 1, 'o': 1, 'w': 1, 'e': 4, 'r': 2,
            'c': 2, 'a': 2, 's': 2, 'u': 1, 'p': 2}
print(count_letters('lowercase/uppercase') == expected)

expected = {'u': 1, 'o': 1, 'i': 1, 's': 1}
print(count_letters('W. E. B. Du Bois') == expected)

print(count_letters('x') == {'x': 1})
print(count_letters('') == {})
print(count_letters('!!!') == {})
"""

# Input: string
# Output: dict with keys representing lowercase chars that appear in string and
# values representing number of their occurances in string

# Algorithm
# Create empty dict counts
# Iterate over chars in string:
#   if char is lowercase:
#       if char is not present in dict:
#           add it to dict and set its value to 1
#       else:
#           increment this letter's count by 1
# return dict

def count_letters(string):
    counts = {}
    for char in string:
        if char.islower():
            counts[char] = counts.get(char, 0) + 1
    return counts        

expected = {'w': 1, 'o': 2, 'e': 3, 'b': 1, 'g': 1, 'n': 1}
print(count_letters('woebegone') == expected)

expected = {'l': 1, 'o': 1, 'w': 1, 'e': 4, 'r': 2,
            'c': 2, 'a': 2, 's': 2, 'u': 1, 'p': 2}
print(count_letters('lowercase/uppercase') == expected)

expected = {'u': 1, 'o': 1, 'i': 1, 's': 1}
print(count_letters('W. E. B. Du Bois') == expected)

print(count_letters('x') == {'x': 1})
print(count_letters('') == {})
print(count_letters('!!!') == {})