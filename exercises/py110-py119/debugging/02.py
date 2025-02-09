"""
Reverse a String
You have a function that is supposed to reverse a string passed as an argument. However, it's not producing the expected output. Explain the bug, and provide a solution.

def reverse_string(string):
    for char in string:
        string = char + string

    return string

print(reverse_string("hello") == "olleh")
"""

# Inside a function we iterate over original string. Inside a loop body we reassign a string to a new value:
# Current character + the string itself. So after first iteration string 'hello' looks like this: 'hhello'.
# The simplest way to fix the code would be to use Python's slicing to reverse the string:

def reverse_string(string):
    return string[::-1]

print(reverse_string("hello") == "olleh")