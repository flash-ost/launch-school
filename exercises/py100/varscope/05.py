"""
What's my value? (Part 5)
What will the following code do and why? Don't run it until you have tried to answer.

a = 1

def my_function():
    print(a)
    a = 2

my_function()
"""

# Since a is also assigned inside the definition, Python considers that we reference a local a inside the print call.
# We will get error about referencing a variable before assigning it.
a = 1

def my_function():
    print(a)
    a = 2

my_function()