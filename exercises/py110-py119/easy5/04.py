"""
How Long Are You?
Write a function that takes a string as an argument and returns a list that contains every word from the string, with each word followed by a space and the word's length. If the argument is an empty string or if no argument is passed, the function should return an empty list.

You may assume that every pair of words in the string will be separated by a single space.

Examples
# All of these examples should print True
words = 'cow sheep chicken'
expected_result = ['cow 3', 'sheep 5', 'chicken 7']
print(word_lengths(words) == expected_result)        # True

words = 'baseball hot dogs and apple pie'
expected_result = ['baseball 8', 'hot 3', 'dogs 4',
                   'and 3', 'apple 5', 'pie 3']
print(word_lengths(words) == expected_result)        # True

words = "It ain't easy, is it?"
expected_result = ['It 2', "ain't 5", 'easy, 5',
                   'is 2', 'it? 3']
print(word_lengths(words) == expected_result)        # True

big_word = 'Supercalifragilisticexpialidocious'
print(word_lengths(big_word) == [f'{big_word} 34'])  # True

print(word_lengths('') == [])                        # True
print(word_lengths() == [])                          # True
"""

## Understanding
# Input: string of words / empty string / no input
# Output: list of strings. Each string contains a single word from input string and length of this word - separated by space.
# If input string is empty or function is called with no arguments, it should return an empty list.

# Implicit requirements from test cases
# Punctuation marks are considered part of the adjacent word: 'is it?' > ['is 2', 'it? 3']
# Word separation is based in spaces

## Data structure
# List

## Algorithm
# If no input, use default argument - empty string
# Split input string into words based on spaces and store in list
# Iterate over list with words:
#   Replace word with new string in the format: f'{word} {word_length}'
# return list of new strings

def word_lengths(string=''):
    return [f'{word} {len(word)}' for word in string.split()]

words = 'cow sheep chicken'
expected_result = ['cow 3', 'sheep 5', 'chicken 7']
print(word_lengths(words) == expected_result)        # True

words = 'baseball hot dogs and apple pie'
expected_result = ['baseball 8', 'hot 3', 'dogs 4',
                   'and 3', 'apple 5', 'pie 3']
print(word_lengths(words) == expected_result)        # True

words = "It ain't easy, is it?"
expected_result = ['It 2', "ain't 5", 'easy, 5',
                   'is 2', 'it? 3']
print(word_lengths(words) == expected_result)        # True

big_word = 'Supercalifragilisticexpialidocious'
print(word_lengths(big_word) == [f'{big_word} 34'])  # True

print(word_lengths('') == [])                        # True
print(word_lengths() == [])                          # True