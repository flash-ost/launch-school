"""
What's my value? (Part 4)
What will the following code do and why? Don't run it until you have tried to answer.

a = 1

def my_function():
    print(a)

my_function()
"""

# We can access global variable inside the local scope, so the code will print 1.
a = 1

def my_function():
    print(a)

my_function()