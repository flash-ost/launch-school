"""
Given the following global dictionary:

students = {'John': 25, 'Jane': 22, 'Doe': 30}
Write a Python function get_age(name) that takes a student's name as an argument and returns their age. If the student's name isn't in the dictionary, the function should return 'Student not found'.
"""
students = {'John': 25, 'Jane': 22, 'Doe': 30}

# def get_age(name):
#     try:
#         return students[name]
#     except KeyError:
#         return 'Student not found'

def get_age(name):
    return students.get(name, 'Student not found')

print(get_age('John'))
print(get_age('Jake'))