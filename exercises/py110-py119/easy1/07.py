"""
Letter Swap
Given a string of words separated by spaces, write a function that swaps the first and last letters of every word.

You may assume that every word contains at least one letter, and that the string will always contain at least one word. You may also assume that each string contains nothing but words and spaces, and that there are no leading, trailing, or repeated spaces.

Examples
print(swap('Oh what a wonderful day it is')
      == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True
"""

## Understanding
# Input: string of words
# Output: strings of words, but first and last letters are swapped
# Explicit rules
# - every word contains at least one letter
# - string always contains at leats 1 word
# - string contains only words and spaces
# - string doesn't contain any leading, trailing or repeated spaces

## Examples
# Case should be preserved ('Abcde' -> 'ebcdA')

## Data Structure
# List to store split words

## Algorithm
# Split string into list of words
# If word has more than one char:
#   swap its first and last char and replace in original version with new one
# Join words back into string
# Return string

def swap(string):
    words = string.split()
    for idx in range(len(words)):
        if len(words[idx]) > 1:
            words[idx] = words[idx][-1] + words[idx][1:-1] + words[idx][0]
    return ' '.join(words)

print(swap('Oh what a wonderful day it is')
      == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True