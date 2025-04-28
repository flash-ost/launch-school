"""
What Are You?
Using the code from the previous exercise, add a __init__ method that prints I'm a cat! when a new Cat object is instantiated.

Code from Previous Exercise
class Cat:
    pass

kitty = Cat()
Expected output
I'm a cat!
"""

class Cat:
    def __init__(self):
        print('I\'m a cat!')

kitty = Cat()
