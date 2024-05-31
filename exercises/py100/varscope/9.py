"""
What's my value? (Part 9)
What will the following code do and why? Don't run it until you have tried to answer.

a = 7

def my_function(b):
    b += 10

my_function(a)
print(a)
"""
# We create a local variable b inside with initial value 7 and then reassign it to 17. 
# print call references global a, so it will print 7.
a = 7

def my_function(b):
    b += 10

my_function(a)
print(a)