"""
Given the following code, create the Person class needed to make the code work as shown:

bob = Person('bob')
print(bob.name)           # bob
bob.name = 'Robert'
print(bob.name)           # Robert
"""

class Person:
    def __init__(self, name):
        self.name = name

bob = Person('bob')
print(bob.name)           # bob
bob.name = 'Robert'
print(bob.name)           # Robert        