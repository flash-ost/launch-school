"""
Colorful Cat
Create a class named Cat that prints a greeting when the greet instance method is invoked. The greeting should include the name and color of the cat. Use a class constant to define the color.

Expected output
Hello! My name is Sophie and I'm a purple cat!
"""
class Cat:
    COLOR = 'purple'

    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f'Hello! My name is {self.name} and I\'m a {Cat.COLOR} cat!')

kitty = Cat('Sophie')
kitty.greet()