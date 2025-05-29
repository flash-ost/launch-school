"""
Question 1
Which of the following are objects in Python? If they are objects, how can you find out what class they belong to?

True
'hello'
[1, 2, 3, 'happy days']
142
{1, 2, 3}
1.2345
"""
# All of these are objects in Python.
# Class can be determined byusing type() function or accessing __class__ attribute
print(type(True))
print(type('hello'))
print(type([1, 2, 3, 'happy days']))
print((142).__class__)
print({1, 2, 3}.__class__)
print((1.2345).__class__)