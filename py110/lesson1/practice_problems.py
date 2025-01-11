"""
Practice Problem 1
Given the tuple:
fruits = ("apple", "banana", "cherry", "date", "banana")
How would you count the number of occurrences of "banana" in the tuple?
"""
# fruits = ("apple", "banana", "cherry", "date", "banana")
# print(fruits.count('banana'))

"""
Practice Problem 2
Consider the set:

numbers = {1, 2, 3, 4, 5, 5, 4, 3}
print(len(numbers))
What is the set's length? Try to answer without running the code.
"""
# 5, since there can be no duplicates in a set
# numbers = {1, 2, 3, 4, 5, 5, 4, 3}
# print(len(numbers))

"""
Practice Problem 3
Given two sets:

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
How would you obtain a set that contains all the unique values from both sets?
"""
# Using union operator |
# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}
# print(a | b)
# Using set.union method
# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}
# print(a is a.union(b))

"""
Practice Problem 4
Given the following code, what would the output be? Try to answer without running the code.

names = ["Fred", "Barney", "Wilma", "Betty", "Pebbles", "Bambam"]
name_positions = {}
for index, name in enumerate(names):
    name_positions[name] = index
print(name_positions)
"""
# Output: dict with list elements as keys and their index numbers as values
# names = ["Fred", "Barney", "Wilma", "Betty", "Pebbles", "Bambam"]
# name_positions = {}
# for index, name in enumerate(names):
#     name_positions[name] = index
# print(name_positions)

"""
Practice Problem 5
Calculate the total age given the following dictionary:

ages = {
    "Herman": 32,
    "Lily": 30,
    "Grandpa": 5843,
    "Eddie": 10,
    "Marilyn": 22,
    "Spot": 237,
}
"""
# Using built-in sum function
# ages = {
#     "Herman": 32,
#     "Lily": 30,
#     "Grandpa": 5843,
#     "Eddie": 10,
#     "Marilyn": 22,
#     "Spot": 237,
# }
# print(sum(ages.values()))

"""
Practice Problem 6
Determine the minimum age from the above ages dictionary.
"""
# Using built-in min function
# ages = {
#     "Herman": 32,
#     "Lily": 30,
#     "Grandpa": 5843,
#     "Eddie": 10,
#     "Marilyn": 22,
#     "Spot": 237,
# }
# print(min(ages.values()))

"""
Practice Problem 7
What would the following code output? Try to answer without running the code.

words = ['ant', 'bear', 'cat']
selected_words = []
for word in words:
    if len(word) > 3:
        selected_words.append(word)

print(selected_words)
"""
# Output: ['bear'], since only this word is over 3 chars long
# words = ['ant', 'bear', 'cat']
# selected_words = []
# for word in words:
#     if len(word) > 3:
#         selected_words.append(word)

# print(selected_words)

"""
Practice Problem 8
Given the following string, create a dictionary that represents the frequency with which each letter occurs. The frequency count should be case-sensitive:

statement = "The Flintstones Rock"
"""
# Remove spaces from string
# Create empty dict
# Iterate over letters in string, populating the dict and updating letters count
# statement = "The Flintstones Rock"
# frequency = {}
# for letter in statement.replace(' ', ''):
    # frequency.setdefault(letter, 0) # method 1
    # frequency[letter] += 1          # method 1
#     frequency[letter] = frequency.get(letter, 0) + 1 # method 2
# print(frequency)    

"""
Practice Problem 9
What is the return value of the list comprehension below? Try to answer without running the code.

[num for num in [1, 2, 3] if num > 1]
"""
# Return value: [2, 3], since we perform selection with num > 1
# print([num for num in [1, 2, 3] if num > 1])

"""
Practice Problem 10
What does the following code print and why?

dictionary = {'a': 'ant', 'b': 'bear'}
print(dictionary.popitem())
"""
# dict.popitem method deletes the last pair from the dict and returns this pair as a tuple
# Code will print: ('b', 'bear')
# dictionary = {'a': 'ant', 'b': 'bear'}
# print(dictionary.popitem())

"""
Practice Problem 11
What does the following code return? Try to answer without running the code.

lst = [1, 2, 3, 4, 5]
lst[:2]
"""
# Code returns a slice, starting at the beginning of the list and ending before index 2: [1, 2]
# lst = [1, 2, 3, 4, 5]
# print(lst[:2])

"""
Practice Problem 12
What would be the output of the below code? Try to answer without running the code.

frozen = frozenset([1, 2, 3, 4, 5])
frozen.add(6)
print(frozen)
"""
# Python will throw an AttributeError exception. frozenset is animmutable data type,
# so unlike set, it doesn't have add method
# frozen = frozenset([1, 2, 3, 4, 5])
# frozen.add(6)
# print(frozen)