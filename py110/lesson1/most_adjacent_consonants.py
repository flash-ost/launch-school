"""
Sort Strings by Most Adjacent Consonants
Given a list of strings, return a new list where the strings are sorted
based on the highest number of adjacent consonants a string contains.
If two strings contain the same highest number of adjacent consonants,
they should retain their original order in relation to each other.
Consonants are considered adjacent if they are next to each other in the same word
or if there is a space between two consonants in adjacent words.
"""

## Understanding the Problem

# Input: list of strings
# Output: sorted list of strings

# Explicit rules:
# - strings in list should be sorted by the highest number of adjacent consonants
# - if strings have the same highest num of adj consonants, they stay in place, no swapping
# - if there is space between consonants, they are considered adjacent
# - based , test cases, single consonant does not affect sort order (['aa', 'baa'] - strings stay as is)

# Implicit rules:
# - strings may contain more than 1 word

# Questions
# - Does case matter? Should we consider consonants adjacent if they have different case?
# - Can string be empty?

## Example and Test Cases

# # my_list = ['aa', 'baa', 'ccaa', 'dddaa']
# print(sort_by_consonant_count(my_list))
# # ['dddaa', 'ccaa', 'aa', 'baa']

# my_list = ['can can', 'toucan', 'batman', 'salt pan']
# print(sort_by_consonant_count(my_list))
# # ['salt pan', 'can can', 'batman', 'toucan']

# my_list = ['bar', 'car', 'far', 'jar']
# print(sort_by_consonant_count(my_list))
# # ['bar', 'car', 'far', 'jar']

# my_list = ['day', 'week', 'month', 'year']
# print(sort_by_consonant_count(my_list))
# # ['month', 'day', 'week', 'year']

# my_list = ['xxxa', 'xxxx', 'xxxb']
# print(sort_by_consonant_count(my_list))
# # ['xxxx', 'xxxb', 'xxxa']

# Test cases don't answer the question about case and whether string can be empty.

## Data structures

# We will work with list that is passed as argument.
# We will also use a dict to keep track of each strings' adjacent consonants count.

## Algorithm

# Create a copy of a alist that was pass as argument. Work only with copy in next steps.
# Create a dict to store each strings' max adjacent consonants.
# Iterate over every word in list:
#   Create a var for max adj consonants, init to 0
#   Create a var for adj consonants, init to 0
#   Iterate over every char in a string:
#       If char is a consonant:
#           adj_cons += 1
#       elif char is space:
#           pass
#       else:
#           if adj_cons > max_adj AND adj_cons > 1:
#               max_adj = adj_cons
#           Reset adj_cons to 0
#   
# Create a list with dict values (num of adj consonants) and sort it in descending order
# Create an empty list.
# Iterate over list with sorted dict values:
#   find a dict key corresponding to given value
#   append new list with key
#   remove key-value pair from list
# Return list of sorted strings.
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'

def max_adjacent(string):
    max_adj = 0
    adj_cons = 0
    for char in string:
        if char in CONSONANTS:
            adj_cons += 1
        elif char == ' ':
            pass
        else:
            if adj_cons > 1 and adj_cons > max_adj:
                max_adj = adj_cons
            adj_cons = 0

    # Catch a case where last adj consonants are at the very end
    if adj_cons > 1 and adj_cons > max_adj:
        max_adj = adj_cons  

    return max_adj        

def sort_by_consonant_count(strings):
    new_list = list(strings)
    new_list.sort(key=max_adjacent, reverse=True)
    return new_list

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