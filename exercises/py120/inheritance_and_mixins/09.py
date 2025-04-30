"""
Method Resolution Path (Part 2)
Using the code below, determine the method resolution order (MRO) when accessing cat1.color. Only list the classes and mix-ins Python will check when searching for the color method. Do not use the mro method.

class Animal:
    pass

class Cat(Animal):
    pass

class Bird(Animal):
    pass

cat1 = Cat()
cat1.color
"""
# 1) Cat
# 2) Animal
# 3) object

class Animal:
    pass

class Cat(Animal):
    pass

class Bird(Animal):
    pass

cat1 = Cat()
print(Cat.mro())