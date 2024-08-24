"""
Practice Problem 1
Consider the following nested dictionary:

munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}
Compute and display the total age of the family's male members. Try working out the answer two ways: first with an ordinary loop, then with a comprehension.

The result should be 444.
"""
munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}
# # # Loop
# # result = 0
# # for person in munsters:
# #     if munsters[person]['gender'] == 'male':
# #         result += munsters[person]['age']
# # print(result)

# # Comprehension
# print(sum([munsters[person]['age'] for person in munsters if munsters[person]['gender'] == 'male']))
# print(sum([person['age'] for person in munsters.values() if person['gender'] == 'male']))

"""
Practice Problem 2
Given the following data structure, return a new list with the same structure, but with the values in each sublist ordered in ascending order. Use a comprehension if you can. (Try using a for loop first.)

lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]
Expected result
[['a', 'b', 'c'], [-3, 2, 11], ['black', 'blue', 'green']]
The string values should be sorted as strings, while the numeric values should be sorted as numbers.
"""
lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]

# # # Loop
# # lst2 = []
# # for el in lst:
# #     lst2.append(sorted(el))
# # print(lst2)    

# # Comprehension
# lst2 = [sorted(el) for el in lst]
# print(lst2)

"""
Practice Problem 3
Given the following data structure, return a new list with the same structure, but with the values in each sublist ordered in ascending order as strings (that is, the numbers should be treated as strings). Use a comprehension if you can. (Try using a for loop first.)

lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]
Expected result
[['a', 'b', 'c'], [-3, 11, 2], ['black', 'blue', 'green']]
"""
lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]
# # # Loop
# # lst2 = []
# # for el in lst:
# #     lst2.append(sorted(el, key=str))
# # print(lst2)    

# # Comprehension
# lst2 = [sorted(el, key=str) for el in lst]
# print(lst2)

"""
Practice Problem 4
Given the following data structure, write some code that defines a dictionary where the key is the first item in each sublist, and the value is the second.

lst = [
    ['a', 1],
    ['b', 'two'],
    ['sea', {'c': 3}],
    ['D', ['a', 'b', 'c']]
]
Expected result
# Pretty printed for clarity
{
    'a': 1,
    'b': 'two',
    'sea': {c: 3},
    'D': ['a', 'b', 'c']
}
"""
# lst = [
#     ['a', 1],
#     ['b', 'two'],
#     ['sea', {'c': 3}],
#     ['D', ['a', 'b', 'c']]
# ]

# dict1 = {key: value for key, value in lst}
# print(dict1)

"""
Practice Problem 5
Given the following data structure, sort the list so that the sub-lists are ordered based on the sum of the odd numbers that they contain. You shouldn't mutate the original list.

lst = [[1, 6, 7], [1, 5, 3], [1, 8, 3]]
Note that the first sublist has the odd numbers 1 and 7; the second sublist has odd numbers 1, 5, and 3; and the third sublist has 1 and 3. Since (1 + 3) < (1 + 7) < (1 + 5 + 3), the sorted list should look like this:

Expected result
[[1, 8, 3], [1, 6, 7], [1, 5, 3]]
Try to use a comprehension in your solution.
"""
# lst = [[1, 6, 7], [1, 5, 3], [1, 8, 3]]
# def odds_sum(lst):
#     return sum([el for el in lst if el % 2 == 1])
# new = [sorted(lst, key=odds_sum)]
# print(new)

"""
Practice Problem 6
Given the following data structure, return a new list identical in structure to the original but, with each number incremented by 1. Do not modify the original data structure. Use a comprehension.

lst = [{'a': 1}, {'b': 2, 'c': 3}, {'d': 4, 'e': 5, 'f': 6}]
Expected result
[{'a': 2}, {'b': 3, 'c': 4}, {'d': 5, 'e': 6, 'f': 7}]
"""
# lst = [{'a': 1}, {'b': 2, 'c': 3}, {'d': 4, 'e': 5, 'f': 6}]
# lst2 = [{key: value + 1 for key, value in dct.items()} for dct in lst]
# print(lst2)

"""
Practice Problem 7
Given the following data structure return a new list identical in structure to the original, but containing only the numbers that are multiples of 3.

lst = [[2], [3, 5, 7, 12], [9], [11, 15, 18]]
The returned list should look like this:

Expected result
[[], [3, 12], [9], [15, 18]]
Try to use a comprehension for this. However, we recommend first trying it without comprehensions.
"""
# lst = [[2], [3, 5, 7, 12], [9], [11, 15, 18]]
# new = [[num for num in sublist if num % 3 == 0] for sublist in lst]
# print(new)

"""
Practice Problem 8
Given the following data structure, write some code to return a list that contains the colors of the fruits and the sizes of the vegetables. The sizes should be uppercase, and the colors should be capitalized.

dict1 = {
    'grape': {
        'type': 'fruit',
        'colors': ['red', 'green'],
        'size': 'small',
    },
    'carrot': {
        'type': 'vegetable',
        'colors': ['orange'],
        'size': 'medium',
    },
    'apricot': {
        'type': 'fruit',
        'colors': ['orange'],
        'size': 'medium',
    },
    'marrow': {
        'type': 'vegetable',
        'colors': ['green'],
        'size': 'large',
    },
}
The return value should look like this:

Expected result
[["Red", "Green"], "MEDIUM", ["Orange"], "LARGE"]
"""
# dict1 = {
#     'grape': {
#         'type': 'fruit',
#         'colors': ['red', 'green'],
#         'size': 'small',
#     },
#     'carrot': {
#         'type': 'vegetable',
#         'colors': ['orange'],
#         'size': 'medium',
#     },
#     'apricot': {
#         'type': 'fruit',
#         'colors': ['orange'],
#         'size': 'medium',
#     },
#     'marrow': {
#         'type': 'vegetable',
#         'colors': ['green'],
#         'size': 'large',
#     },
# }
# lst = [[color.capitalize() for color in inner_dict['colors']]
#                             if inner_dict['type'] == 'fruit'
#                             else inner_dict['size'].upper()
#                             for inner_dict in dict1.values()]
# print(lst)

"""
Practice Problem 9
This problem may prove challenging. Try it, but don't stress about it. If you don't solve it in 20 minutes, you can look at the answer.

Given the following data structure, write some code to return a list that contains only the dictionaries where all the numbers are even.

lst = [
    {'a': [1, 2, 3]},
    {'b': [2, 4, 6], 'c': [3, 6], 'd': [4]},
    {'e': [8], 'f': [6, 10]},
]
Expected result
[{e: [8], f: [6, 10]}]
"""
# lst = [
#     {'a': [1, 2, 3]},
#     {'b': [2, 4, 6], 'c': [3, 6], 'd': [4]},
#     {'e': [8], 'f': [6, 10]},
# ]

# def all_even(lst):
#     for sublist in lst:
#         for num in sublist:
#             if num % 2 != 0:
#                 return False
#     return True
        
# evens = [num_dict for num_dict in lst if all_even(list(num_dict.values()))]
# print(evens)

"""
Practice Problem 10
A UUID (Universally Unique Identifier) is a type of identifier often used to uniquely identify items, even when some of those items were created on a different server or by a different application. That is, without any synchronization, two or more computer systems can create new items and label them with a UUID with no significant risk of stepping on each other's toes. It accomplishes this feat through massive randomization. The number of possible UUID values is approximately 3.4 X 10E38, which is a huge number. The chance of a conflict, a "collision", is vanishingly small with such a large number of possible values.

Each UUID consists of 32 hexadecimal characters (the digits 0-9 and the letters a-f) represented as a string. The value is typically broken into 5 sections in an 8-4-4-4-12 pattern, e.g., 'f65c57f6-a6aa-17a8-faa1-a67f2dc9fa91'.

Note that our description of UUIDs is a simplified description of how UUIDs are formed. There are several UUID versions, each with some non-random characteristics in some of the bits. These different versions can play a part in certain applications.

Write a function that takes no arguments and returns a string that contains a UUID.
"""
# from random import choice
# def uuid():
#     CHARS = '0123456789abcdef'
#     pattern = [8, 4, 4, 4, 12]
#     sections = []
#     for num in pattern:
#         section = ''
#         for count in range(num):
#             section += choice(CHARS)
#         sections.append(section)

#     return '-'.join(sections)  
# print(uuid())

"""
Practice Problem 11
The following dictionary has list values that contains strings. Write some code to create a list of every vowel (a, e, i, o, u) that appears in the contained strings, then print it.

dict1 = {
    'first':  ['the', 'quick'],
    'second': ['brown', 'fox'],
    'third':  ['jumped'],
    'fourth': ['over', 'the', 'lazy', 'dog'],
}

# Your code goes here

print(list_of_vowels)
# ['e', 'u', 'i', 'o', 'o', 'u', 'e', 'o', 'e', 'e', 'a', 'o']
"""
VOWELS = 'aeiou'
dict1 = {
    'first':  ['the', 'quick'],
    'second': ['brown', 'fox'],
    'third':  ['jumped'],
    'fourth': ['over', 'the', 'lazy', 'dog'],
}
# # Nested Loops
# vowels = []
# for lst in dict1.values():
#     for word in lst:
#         for char in word:
#             if char in VOWELS:
#                 vowels.append(char)

# print(vowels)

# Comprehension
vowels = [char for key in dict1
               for word in dict1[key]
               for char in word 
               if char in VOWELS]
print(vowels)


