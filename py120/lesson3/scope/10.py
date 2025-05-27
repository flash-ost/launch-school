"""
Consider the following code:

class Bird:
    def __init__(self, species):
        self.species = species

class Sparrow(Bird):
    def __init__(self, species, color):
        self.color = color

birdie = Sparrow("sparrow", "brown")
print(birdie.species)               # What will this output?
Without running the above code, what will it output? If it raises an error, explain why and how to fix it.
"""
# Python will raise AttributeError when executing print(birdie.species), since
# Sparrow class has its own init method that overrides init of superclass.
# Inside Sparrow's init we don't call super().__init__() and don't create species attribute,
# so it doesn't exist. Solution: add super().__init__(species) to Sparrow's init method.
class Bird:
    def __init__(self, species):
        self.species = species

class Sparrow(Bird):
    def __init__(self, species, color):
        super().__init__(species)
        self.color = color

birdie = Sparrow("sparrow", "brown")
print(birdie.species)