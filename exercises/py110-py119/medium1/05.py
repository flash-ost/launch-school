"""
Word to Digit
Write a function that takes a string as an argument and returns that string with every occurrence of a "number word" -- 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine' -- converted to its corresponding digit character.

You may assume that the string does not contain any punctuation.

Example
message = 'Please call me at five five five one two three four'
print(word_to_digit(message) == "Please call me at 5 5 5 1 2 3 4")
# Should print True
"""

## Understanding
# Input: string
# Output: string with every occurence of number as word converted ti its corresponding digit character

# Explicit rules
# - input string won't contain any punctuation

## Algorithm
# Create a dictionary with numbers 0-9 in word form as keys and corresponding number characters as values
# Iterate over dictionary keys:
#   if key is present in string:
#       replace all occurences of key with corresponding value
# Return modified string

def word_to_digit(string):
    numbers = { 'zero': '0',
                'one': '1',
                'two': '2',
                'three': '3',
                'four': '4',
                'five': '5',
                'six': '6',
                'seven': '7',
                'eight': '8',
                'nine': '9' }
    for word in numbers:
        if word in string:
            string = string.replace(word, numbers[word])        
    return string

message = 'Please call me at five five five one two three four'
print(word_to_digit(message) == "Please call me at 5 5 5 1 2 3 4")

message = 'Please call me at five, five, five, one, two, three, four.'
print(word_to_digit(message) == "Please call me at 5, 5, 5, 1, 2, 3, 4.")     