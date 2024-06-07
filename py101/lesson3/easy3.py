"""
Question 1
Write two different ways to remove all of the elements from the following list:

numbers = [1, 2, 3, 4]
"""
# numbers = [1, 2, 3, 4]
# # del numbers[::]
# # numbers.clear()
# while numbers:
#    numbers.pop()
# print(numbers)

"""
Question 2
What will the following code output?

print([1, 2, 3] + [4, 5])
Try to answer without running the code.
"""
# # The code will output a single list [1, 2, 3, 4, 5]
# print([1, 2, 3] + [4, 5])

"""
Question 3
What will the following code output?

str1 = "hello there"
str2 = str1
str2 = "goodbye!"
print(str1)
Try to answer without running the code.
"""
# # The code will output 'hello there'
# str1 = "hello there"
# str2 = str1
# str2 = "goodbye!"
# print(str1)

"""
Question 4
What will the following code output?

my_list1 = [{"first": "value1"}, {"second": "value2"}, 3, 4, 5]
my_list2 = my_list1.copy()
my_list2[0]['first'] = 42
print(my_list1)
Try to answer without running the code.
"""
# # The code will output [{"first": 45}, {"second": "value2"}, 3, 4, 5] | Shallow copying doesn't data of nested objects, so my_list2[0] and my_list1[0] point to the same object in memory.
# my_list1 = [{"first": "value1"}, {"second": "value2"}, 3, 4, 5]
# my_list2 = my_list1.copy()
# my_list2[0]['first'] = 42
# print(my_list1)

"""
Question 5
The following function unnecessarily uses two return statements to return boolean values. Can you rewrite this function so it only has one return statement and does not explicitly use either True or False?

def is_color_valid(color):
    if color == "blue" or color == "green":
        return True
    else:
        return False
Try to come up with two different solutions.
"""
# def is_color_valid(color):
#     return color == "blue" or color == "green"

# def is_color_valid(color):
#     return color in ["blue", "green"]