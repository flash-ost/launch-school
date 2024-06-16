"""
What's my value? (Part 7)
What will the following code do and why? Don't run it until you have tried to answer.

a = 1

def my_function():
    global a
    a = 2

my_function()
print(a)
"""

# 'global' keyword is used inside the function definition, so both in function and an call to print we reference a global variable.
# The code will print 2.

a = 1

def my_function():
    global a
    a = 2

my_function()
print(a)