"""
Continuing with our Person class definition, what do you think the following code prints?

bob = Person('Robert Smith')
print(f"The person's name is: {bob}")

Let's override the str function for Person objects by defining a magic method, __str__, in the Person class:

class Person:
   # Code omitted for brevity.

    def __str__(self):
        return self.name
Now, what does the below output?

bob = Person('Robert Smith')
print(f"The person's name is: {bob}")
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

    def __str__(self):
        return self.name

bob = Person('Robert Smith')
print(f"The person's name is: {bob}") 