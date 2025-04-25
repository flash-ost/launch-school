
"""
How do we create a class and an object in Python?

Write a program that defines a class and creates two objects from that class. The class should have at least one instance variable that gets initialized by the initializer.

What class you create doesn't matter, provided it satisfies the above requirements.
"""

class Car:
    def __init__(self, model, year):
        self.model = model
        self.year = year

vw = Car('Volkswagen', 1999)
nissan = Car('Nissan', 2006)
print(f'{vw.model}, {vw.year}')
print(f'{nissan.model}, {nissan.year}')