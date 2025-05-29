"""
Question 5
Which of the following classes would create objects that have an instance variable. How do you know?

class Fruit:
    def __init__(self, name):
        my_name = name

class Pizza:
    def __init__(self, name):
        self.my_name = name
"""
# Only Pizza class will create objects that have instance variable name
# because it uses proper self. prefix. my_name in Fruit's init is just a local variable.
class Fruit:
    def __init__(self, name):
        my_name = name

class Pizza:
    def __init__(self, name):
        self.my_name = name

diabola = Pizza('diabola')
mango = Fruit('mango')

print(diabola.my_name) # diabola
print(mango.my_name) # AttributeError