"""
Problem 13
Create a function that takes two strings as arguments and returns True if some portion of the characters in the first string can be rearranged to match the characters in the second. Otherwise, the function should return False.

You may assume that both string arguments only contain lowercase alphabetic characters. Neither string will be empty.

Examples
print(unscramble('ansucchlohlo', 'launchschool') == True)
print(unscramble('phyarunstole', 'pythonrules') == True)
print(unscramble('phyarunstola', 'pythonrules') == False)
print(unscramble('boldface', 'coal') == True)
The above tests should each print True.
"""

# Input: 2 non-empty string consisting solely of lowercase alphabetic characters
# Output: boolean representing whether some portion of the characters in the first string can be rearranged to match the characters in the second

# Algorithm
# Iterate over chars in second string and create a dictionary: keys - letters, values = number of occurences in string
# Iterate over keys in dict
#   if number of occurences of current key in string 1 is less than number of occurences in string 2:
#       return False
# return True

def unscramble(str1, str2):
    occurrences = {}
    for char in str2:
        occurrences[char] = occurrences.get(char, 0) + 1

    for key in occurrences:
        if str1.count(key) < occurrences[key]:
            return False
    return True   

print(unscramble('ansucchlohlo', 'launchschool') == True)
print(unscramble('phyarunstole', 'pythonrules') == True)
print(unscramble('phyarunstola', 'pythonrules') == False)
print(unscramble('boldface', 'coal') == True)