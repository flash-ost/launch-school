"""
Hello, Sophie! (Part 1)
Using the code from the previous exercise, add a parameter to __init__ that provides a name for the Cat object. Use an instance variable to print a greeting with the provided name. (You can remove the code that displays I'm a cat!.)

Code from Previous Exercise
class Cat:
    def __init__(self):
        print("I'm a cat!")

kitty = Cat('Sophie')
Expected output
Hello! My name is Sophie!
"""
class Cat:
    def __init__(self, name):
        self.name = name
        print(f'Hello! My name is {self.name}!')

kitty = Cat('Sophie')