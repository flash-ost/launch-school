"""
Using the class definition from problem 3, let's create some more people (Person objects):

bob = Person('Robert Smith')
rob = Person('Robert Smith')
Without adding any code to the Person class, we want to compare bob and rob to see whether they both have the same name. How can we make this comparison?
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

bob = Person('Robert Smith')
rob = Person('Robert Smith')
print(bob.name == rob.name)        