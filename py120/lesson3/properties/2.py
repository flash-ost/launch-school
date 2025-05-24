"""
Update your answer from problem 1 to disallow empty strings. You should raise a ValueError. Be sure to test your code.
"""
class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError('Name must be a string.')
        
        if not name:
            raise ValueError('Name can\'t be empty.')
        
        self._name = name

john = Person('John')
# noname = Person('')
john.name = ''