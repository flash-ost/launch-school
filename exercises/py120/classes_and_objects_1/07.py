"""
Privacy
Using the code snippet provided below, modify the instance variable name to indicate to developers that it is intended for internal use only.

class Cat:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello! My name is {self.name}!")

kitty = Cat('Sophie')
kitty.greet()
Expected output
Hello! My name is Sophie!
"""
class Cat:
    def __init__(self, name):
        self._name = name

    def greet(self):
        print(f"Hello! My name is {self._name}!")

kitty = Cat('Sophie')
kitty.greet()