"""
Sort Strings by Most Adjacent Consonants
Given a list of strings, sort the list based on the highest number of adjacent consonants a string contains and return the sorted list. If two strings contain the same highest number of adjacent consonants, they should retain their original order in relation to each other. Consonants are considered adjacent if they are next to each other in the same word or if there is a space between two consonants in adjacent words.
"""

## Understanding
# Input: list of strings
# Output: list of strings sorted by highest number of adjacent consonants a string contains

# Explicit rules
# - If two strings contain the same highest number of adjacent consonants, they should retain
#   their original order in relation to each other
# - Consonants are considered adjacent if they are next to each other in the same word
#   or if there is a space between two consonants in adjacent words

# Questions
# Should we take letter case into account?
# Should we return the same object (perform sorting in-place) or a new one?
# Can there be just one space between consonants or more?

# Info from test cases
# - There won't be empty lists or strings
# - Max 1 space between words
# - Strings may contain multiple words
# - All letters in strings are lowercase
# - Sorting must be performed in descending order
# - Single consonants in a string do not affect sort order in comparison to strings 
#   with no consonants. Only adjacent consonants affect sort order (case 1: 'aa', 'baa')

## Data Structure
# List

## Algorithm
# Helper function most_adjacents(string):
#   Remove spaces from string
#   Initialize most_adjacent_consonants to 1 (as we don't want to take single consonants into account)
#   Initialize adjacent_consonants counter to 0
#   Iterate over every char in string:
#       if char is consonant:
#           increment adjacent_consonants counter by 1
#       else:
#           if adjacent_consonants > most_adjacent_consonants:
#              set adjacent_consonants to adjacent_consonants
#           reset adjacent_consonants to 0
#   Account for case when the last char is consonant that forms the longest streak
#   of adjacent consonants:
#   if adjacent_consonants > most_adjacent_consonants:
#              set adjacent_consonants to adjacent_consonants
#   return most_adjacent_consonants

# Main function:
#   Copy list
#   Sort the copy in descending order, based on output from most_adjacents
#   Return sorted copy of a list

def most_adjacents(string):
    CONSONANTS = 'bcdfghjklmnpqrstvwx'

    string = string.replace(' ', '')
    most_adjacent_consonants = 1
    adjacent_consonants = 0
    for char in string:
        if char in CONSONANTS:
            adjacent_consonants += 1
        else:
            if adjacent_consonants > most_adjacent_consonants:
                most_adjacent_consonants = adjacent_consonants
            adjacent_consonants = 0
    # Account for case when the last char is consonant that forms the longest streak of adjacent consonants
    if adjacent_consonants > most_adjacent_consonants:
        most_adjacent_consonants = adjacent_consonants
    
    return most_adjacent_consonants

def sort_by_consonant_count(lst):
    sorted_list = list(lst)
    sorted_list.sort(key=most_adjacents, reverse=True)
    return sorted_list

my_list = ['aa', 'baa', 'ccaa', 'dddaa']
print(sort_by_consonant_count(my_list))
# ['dddaa', 'ccaa', 'aa', 'baa']

my_list = ['can can', 'toucan', 'batman', 'salt pan']
print(sort_by_consonant_count(my_list))
# ['salt pan', 'can can', 'batman', 'toucan']

my_list = ['bar', 'car', 'far', 'jar']
print(sort_by_consonant_count(my_list))
# ['bar', 'car', 'far', 'jar']

my_list = ['day', 'week', 'month', 'year']
print(sort_by_consonant_count(my_list))
# ['month', 'day', 'week', 'year']

my_list = ['xxxa', 'xxxx', 'xxxb']
print(sort_by_consonant_count(my_list))
# ['xxxx', 'xxxb', 'xxxa']

print(most_adjacents('day'))
print(most_adjacents('week'))