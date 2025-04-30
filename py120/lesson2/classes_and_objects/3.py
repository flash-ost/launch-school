"""
Add a new setter property for name that takes either a first name or full name, and knows how to set the first_name and last_name properties appropriately. Use the following code to test your code:

bob = Person('Robert')
print(bob.name)             # Robert
print(bob.first_name)       # Robert
print(repr(bob.last_name))  # ''
bob.last_name = 'Smith'
print(bob.name)             # Robert Smith

bob.name = 'Prince'
print(bob.first_name)       # Prince
print(repr(bob.last_name))  # ''

bob.name = 'John Adams'
print(bob.first_name)       # John
print(bob.last_name)        # Adams
"""
class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return f'{self.first_name} {self.last_name}'
    
    @name.setter
    def name(self, name):
        full_name = name.split()
        self.first_name = full_name[0]
        self.last_name = full_name[1] if len(full_name) > 1 else ''

bob = Person('Robert')
print(bob.name)             # Robert
print(bob.first_name)       # Robert
print(repr(bob.last_name))  # ''
bob.last_name = 'Smith'
print(bob.name)             # Robert Smith

bob.name = 'Prince'
print(bob.first_name)       # Prince
print(repr(bob.last_name))  # ''

bob.name = 'John Adams'
print(bob.first_name)       # John
print(bob.last_name)        # Adams    