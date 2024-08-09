"""
Letter Counter (Part 2)
Modify the word_sizes function from the previous exercise to exclude non-letters when determining word size. For instance, the word size of "it's" is 3, not 4.

Examples
# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 2, 3: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 3})

string = 'Humpty Dumpty sat on a w@ll'
print(word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1})

string = "What's up doc?"
print(word_sizes(string) == {5: 1, 2: 1, 3: 1})

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
# Iterate over words:
#   - create empty string
#   - iterate over chars in word:
#       - if char is a letter, add it to new string
#   - replace current el with a new string (with letters only)
# Create empty dict
# Iterate over list elements:
#   - calculate length of word
#   - if such length is already in dict, increment value
#   - else create new entry and set value to 1
# Return dict

def word_sizes(string):
    # First version
    # words = string.split()

    # # Clean words
    # for idx in range(len(words)):
    #     clean_word = ''
    #     for char in words[idx]:
    #         if char.isalpha():
    #             clean_word += char
    #     words[idx] = clean_word   

    # # Populate dict
    # sizes = {}
    # for word in words:
    #     size = len(word)
    #     length = len(word)
    #     sizes.setdefault(length, 0)
    #     sizes[length] += 1
    # return sizes 
    # 
    # Shorter version
    sizes = {}
    for word in string.split():
        clean = ''.join(char for char in word if char.isalpha())
        length = len(clean)
        sizes[length] = sizes.get(length, 0) + 1 
    return sizes    

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 2, 3: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 3})

string = 'Humpty Dumpty sat on a w@ll'
print(word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1})

string = "What's up doc?"
print(word_sizes(string) == {5: 1, 2: 1, 3: 1})

print(word_sizes('') == {})    