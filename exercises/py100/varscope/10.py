"""
What's my value? (Part 10)
What will the following code do and why? Don't run it until you have tried to answer.

b = [1, 2, 3]

def my_function():
    b[0] = 10

my_function()
print(b)
"""
# List is a mutable data type. Since we mutate the value of it's first element inside the function, print's output will be [10, 2, 3]
b = [1, 2, 3]

def my_function():
    b[0] = 10

my_function()
print(b)