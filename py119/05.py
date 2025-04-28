"""
Problem 5
Create a function that takes a string argument and returns the character that occurs most often in the string. If there are multiple characters with the same greatest frequency, return the one that appears first in the string. When counting characters, consider uppercase and lowercase versions to be the same.

Examples
print(most_common_char('Hello World') == 'l')
print(most_common_char('Mississippi') == 'i')
print(most_common_char('Happy birthday!') == 'h')
print(most_common_char('aaaaaAAAA') == 'a')

my_str = 'Peter Piper picked a peck of pickled peppers.'
print(most_common_char(my_str) == 'p')

my_str = 'Peter Piper repicked a peck of repickled peppers. He did!'
print(most_common_char(my_str) == 'e')
"""

# Input: string
# Output: string consisting of letter that occurs most often in the string
# Uppercase and lowercase versions should be counted as the same letter
# If several letters with the same greatest frequency, return the one that appeared first
# Return letter should be lowercase even if it first appeared in uppercase

# Algorithm
# Create empty dict frequency
# Iterate over string:
#   if current letter is not in dict:
#       add it to dict as key and set value 1
#   else:
#       increment corresponding value by 1
# convert key-value pairs to list of tuples
# sort list in reverse order based on number (second element) in each tuple
# return a letter (first element) of the first tuple

def get_frequency(pair):
    return pair[1]

def most_common_char(string):
    frequency = {}
    for char in string:
        if char.isalpha():
            lower = char.lower()
            frequency[lower] = frequency.get(lower, 0) + 1

    pairs = list(frequency.items())
    pairs.sort(key=get_frequency, reverse=True)
    return pairs[0][0]

print(most_common_char('Hello World') == 'l')
print(most_common_char('Mississippi') == 'i')
print(most_common_char('Happy birthday!') == 'h')
print(most_common_char('aaaaaAAAA') == 'a')

my_str = 'Peter Piper picked a peck of pickled peppers.'
print(most_common_char(my_str) == 'p')

my_str = 'Peter Piper repicked a peck of repickled peppers. He did!'
print(most_common_char(my_str) == 'e')