"""
What's my value? (Part 2)
What will the following code do and why? Don't run it until you have tried to answer.

x = 10

def my_function():
    x = x + 5
    print(x)

my_function()
"""

# Variable inside the function definition is local, so trying to initialize it with expression x + 5 will lead to an error
# (referencing before assingment).
x = 10

def my_function():
    x = x + 5
    print(x)

my_function()