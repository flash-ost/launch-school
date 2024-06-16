"""
What's my value? (Part 6)
What will the following code do and why? Don't run it until you have tried to answer.

a = 1

def my_function():
    a = 2

my_function()
print(a)
"""
# We create a local variable inside the function. Call to print is referencing the global a, so the output will be 1.
a = 1

def my_function():
    a = 2

my_function()
print(a)