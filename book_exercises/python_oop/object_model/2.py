"""
Given an instance of a Foo object, show two ways to print I am a Foo object without hardcoding the word Foo.
"""


class Foo:
    def __init__(self):
        print(f'I am a {type(self).__name__} object')
        print(f'I am a {self.__class__.__name__} object')

foo = Foo()  