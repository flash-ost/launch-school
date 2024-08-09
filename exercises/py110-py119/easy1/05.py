"""
Letter Counter (Part 1)
Write a function that takes a string consisting of zero or more space-separated words and returns a dictionary that shows the number of words of different sizes.

Words consist of any sequence of non-space characters.

Examples
# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 1, 3: 1, 6: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 1, 7: 2})

string = 'Humpty Dumpty sat on a wall'
print(word_sizes(string) == {6: 2, 3: 1, 2: 1, 1: 1, 4: 1})

string = "What's up doc?"
print(word_sizes(string) == {6: 1, 2: 1, 4: 1})

print(word_sizes('') == {})
"""

## Understanding
# Input: string of 0+ space-separated words
# Output: dict (keys: num of charsin word, values: num of words that have corresponding length)
# Word can consist of any chars except for spaces
# Spaces - separator

## Test Cases
# empty string - empty dict

## Data Structure
# List for splitted words, dictionary for counting words of certain length

## Algorithm
# Split input string into list of words
# Create empty dict
# Iterate over list elements:
#   - calculate length of word
#   - if such length is already in dict, increment value
#   - else create new entry and set value to 1
# Return dict

def word_sizes(string):
    words = string.split()
    sizes = {}
    
    for word in words:
        size = len(word)
        length = len(word)
        sizes.setdefault(length, 0)
        sizes[length] += 1

    return sizes        

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 1, 3: 1, 6: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 1, 7: 2})

string = 'Humpty Dumpty sat on a wall'
print(word_sizes(string) == {6: 2, 3: 1, 2: 1, 1: 1, 4: 1})

string = "What's up doc?"
print(word_sizes(string) == {6: 1, 2: 1, 4: 1})

print(word_sizes('') == {})