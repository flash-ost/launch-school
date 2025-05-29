"""
Question 10
Suppose you have the following class:

class Cat:
    _cats_count = 0

    def __init__(self, type):
        self.type = type
        self.__class__._cats_count += 1

    @classmethod
    def cats_count(cls):
        return cls._cats_count
Explain what the _cats_count variable is, what it does in this class, and how it works. Write some code to test your theory.
"""
# _cats_count is a class variable used for counting the number of Cat class objects.
# Each time a Cat class object is created, we increment _cats_count with
# self.__class__._cats_count += 1 in __init__ method
class Cat:
    _cats_count = 0

    def __init__(self, type):
        self.type = type
        self.__class__._cats_count += 1

    @classmethod
    def cats_count(cls):
        return cls._cats_count

print(Cat.cats_count())
cat1 = Cat('Persian')
print(Cat.cats_count())
cat2 = Cat('Khao Manee')
print(Cat.cats_count())
