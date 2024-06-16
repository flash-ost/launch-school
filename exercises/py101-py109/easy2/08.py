"""
Odd Lists
Write a function that returns a list that contains every other element of a list that is passed in as an argument. The values in the returned list should be those values that are in the 1st, 3rd, 5th, and so on elements of the argument list.

Examples
print(oddities([2, 3, 4, 5, 6]) == [2, 4, 6])  # True
print(oddities([1, 2, 3, 4]) == [1, 3])        # True
print(oddities(["abc", "def"]) == ['abc'])     # True
print(oddities([123]) == [123])                # True
print(oddities([]) == [])                      # True
Bonus question: Try to solve the problem using list slicing.
"""
# def oddities(list):
#     return list[::2]

# print(oddities([2, 3, 4, 5, 6]) == [2, 4, 6])  # True
# print(oddities([1, 2, 3, 4]) == [1, 3])        # True
# print(oddities(["abc", "def"]) == ['abc'])     # True
# print(oddities([123]) == [123])                # True
# print(oddities([]) == [])                      # True

"""
Further Exploration
Write a companion function that returns the 2nd, 4th, 6th, and so on elements of a list.

Try to solve this differently from the exercise described above.
"""
def evens(list):
    # return list[1::2]
    new_list = []
    for index in range(1, len(list), 2):
        new_list.append(list[index])
    return new_list
        
print(evens([1, 2, 3, 4, 5, 6]))