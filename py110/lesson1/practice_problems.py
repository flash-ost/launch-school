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

numbers = {1, 2, 3, 4, 5, 5, 4, 3}
print(len(numbers))
What is the set's length? Try to answer without running the code.
"""
# # 5, cuz no duplicate values
# numbers = {1, 2, 3, 4, 5, 5, 4, 3}
# print(len(numbers))

"""
Practice Problem 3
Given two sets:

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
How would you obtain a set that contains all the unique values from both sets?
"""
# # Method 1
# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}

# # Method 1
# c = a | b

# # Method 2
# c = a.union(b)
# print(c)

"""
Practice Problem 4
Given the following code, what would the output be? Try to answer without running the code.

names = ["Fred", "Barney", "Wilma", "Betty", "Pebbles", "Bambam"]
name_positions = {}
for index, name in enumerate(names):
    name_positions[name] = index
print(name_positions)
"""
# # {'Fred': 0, 'Barney': 1, 'Wilma': 2, 'Betty': 3, 'Pebbles': 4, 'Bambam': 5}
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
# # ['bear']
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
The output should resemble the following:

# Pretty printed for clarity
{
    'T': 1,
    'h': 1,
    'e': 2,
    'F': 1,
    'l': 1,
    'i': 1,
    'n': 2,
    't': 2,
    's': 2,
    'o': 2,
    'R': 1,
    'c': 1,
    'k': 1
}
Your program may output the pairs in a different order.
"""

# statement = "The Flintstones Rock"
# frequency = {}
# for char in statement:
#     if char.isalpha():
#         # # Method 1
#         # frequency.setdefault(char, 0)
#         # frequency[char] += 1

#         # Method 2
#         frequency[char] = frequency.get(char, 0) + 1

# print(frequency)

"""
Practice Problem 9
What is the return value of the list comprehension below? Try to answer without running the code.

[num for num in [1, 2, 3] if num > 1]
"""
# # [2, 3]
# print([num for num in [1, 2, 3] if num > 1])

"""
Practice Problem 10
What does the following code print and why?

dictionary = {'a': 'ant', 'b': 'bear'}
print(dictionary.popitem())
"""
# popitem method deletes last key-value pair and returns it. Output: ('b', 'bear')
dictionary = {'a': 'ant', 'b': 'bear'}
print(dictionary.popitem())

"""
Practice Problem 11
What does the following code return? Try to answer without running the code.

lst = [1, 2, 3, 4, 5]
lst[:2]
"""
# # Slice from 0-indexed element to 2-indexed (excluding): [1, 2]
# lst = [1, 2, 3, 4, 5]
# print(lst[:2])

"""
Practice Problem 12
What would be the output of the below code? Try to answer without running the code.

frozen = frozenset([1, 2, 3, 4, 5])
frozen.add(6)
print(frozen)
"""
# Frozen sets are immutable, so there will be an error, since frozenset doesn't have add method 
frozen = frozenset([1, 2, 3, 4, 5])
frozen.add(6)
print(frozen)