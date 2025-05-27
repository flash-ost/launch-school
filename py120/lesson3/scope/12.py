"""
Consider the following code:

class Cat:
    sound = "meow"

    @classmethod
    def make_sound(cls):
        return cls.sound

class Lion(Cat):
    sound = "roar"

print(Lion.make_sound())
Answer the following question without running the code.

What will this code output, and why?
"""
# The output will be 'roar'.
# Inside classmethod make_sound we reference a sound attribute of the current class.
# Lion class inherits from Cat class, so when we call make_sound from the Lion class,
# cls.sound inside the method references the sound class attribute of Lion.
class Cat:
    sound = "meow"

    @classmethod
    def make_sound(cls):
        return cls.sound

class Lion(Cat):
    sound = "roar"

print(Lion.make_sound())