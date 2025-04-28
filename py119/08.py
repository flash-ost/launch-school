"""
Problem 8
Create a function that takes a non-empty string as an argument. The string consists entirely of lowercase alphabetic characters. The function should return the length of the longest vowel substring. The vowels of interest are "a", "e", "i", "o", and "u".

Examples
print(longest_vowel_substring('cwm') == 0)
print(longest_vowel_substring('many') == 1)
print(longest_vowel_substring('launchschoolstudents') == 2)
print(longest_vowel_substring('eau') == 3)
print(longest_vowel_substring('beauteous') == 3)
print(longest_vowel_substring('sequoia') == 4)
print(longest_vowel_substring('miaoued') == 5)
The above tests should each print True.
"""

# Input: non-empty string, only lowercase alphabetic characters
# Output: length of longest vowel substring

# Algorithm
# Initialize count to 0
# Initialize string vowels containing English alphabet vowels
# Initalize max_count to 0
# Iterate over chars in input string:
#   if char is present in vowels:
#       increment count by 1
#   else:
#       if count > max_count:
#           set max_count to count
#       set count to 0
# if count > max_count:
#   set max_count to count
# Return max_count

def longest_vowel_substring(string):
    count = max_count = 0
    vowels = ["a", "e", "i", "o", "u"]
    for char in string:
        if char in vowels:
            count += 1
        else:
            if count > max_count:
                max_count = count
            count = 0
    if count > max_count:
        max_count = count
    return max_count            

print(longest_vowel_substring('cwm') == 0)
print(longest_vowel_substring('many') == 1)
print(longest_vowel_substring('launchschoolstudents') == 2)
print(longest_vowel_substring('eau') == 3)
print(longest_vowel_substring('beauteous') == 3)
print(longest_vowel_substring('sequoia') == 4)
print(longest_vowel_substring('miaoued') == 5)