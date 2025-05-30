"""
Question 7
What would happen if you ran the following code? Don't run it until you've checked your answer:

class Television:
    @classmethod
    def manufacturer(cls):
        return 'Amazon'

    def model(self):
        return 'Omni Fire'

tv = Television()
print(tv.manufacturer())
print(tv.model())

print(Television.manufacturer())
print(Television.model())
"""
class Television:
    @classmethod
    def manufacturer(cls):
        return 'Amazon'

    def model(self):
        return 'Omni Fire'

tv = Television()
print(tv.manufacturer()) # 'Amazon' - we can call class method using instance object
print(tv.model()) # 'Omni Fire' - calling instance method

print(Television.manufacturer()) # 'Amazon' - calling class method through class
print(Television.model()) # TypeError (missing argument self) - can't call instance method from class