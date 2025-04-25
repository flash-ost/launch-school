class Person:
    @classmethod
    def validate(cls, name):
        if not name.isalpha():
            raise ValueError('Name must be alphabetic')

    def __init__(self, first, last):
        self._set_names(first, last)

    @property
    def name(self):
        full_name = f'{self._first.capitalize()} {self._last.capitalize()}'
        return full_name
    
    @name.setter
    def name(self, names):
        first, last = names
        self._set_names(first, last)

    def _set_names(self, first, last):
        self.validate(first)
        self.validate(last)
        self._first = first
        self._last = last
    
# # Test 1    
# actor = Person('Mark', 'Sinclair')
# print(actor.name)              # Mark Sinclair
# actor.name = ('Vin', 'Diesel')
# print(actor.name)              # Vin Diesel
# actor.name = ('', 'Diesel')
# # ValueError: Name must be alphabetic.

# # Test 2
# character = Person('annIE', 'HAll')
# print(character.name)          # Annie Hall
# character = Person('Da5id', 'Meier')
# # ValueError: Name must be alphabetic.

# Test 3
friend = Person('Lynn', 'Blake')
print(friend.name)             # Lynn Blake
friend.name = ('Lynn', 'Blake-John')
# ValueError: Name must be alphabetic.