"""
Nobility
Now that we have a WalkMixin mix-in, we are given a new challenge. Apparently some of our users are nobility, and the regular way of walking simply isn't good enough. Nobility struts.

We need a new class Noble that shows the title and name when walk is called. We also require access to name and title; they are needed for other purposes that we aren't showing here.

byron = Noble("Byron", "Lord")
print(byron.walk())  # "Lord Byron struts forward"
print(byron.name)    # "Byron"
print(byron.title)   # "Lord"
"""

class WalkMixin:
    def walk(self):
        return f'{self.name} {self.gait()} forward'

class Noble(WalkMixin):
    def __init__(self, name, title):
        self.name = name
        self.title = title

    def gait(self):
        return 'struts'
    
    def walk(self):
        return f'{self.title} {super().walk()}'
    
class Person(WalkMixin):
    def __init__(self, name):
        self.name = name

    def gait(self):
        return "strolls"

class Cat(WalkMixin):
    def __init__(self, name):
        self.name = name

    def gait(self):
        return "saunters"

class Cheetah(WalkMixin):
    def __init__(self, name):
        self.name = name

    def gait(self):
        return "runs"    

mike = Person("Mike")
print(mike.walk())  # Expected: "Mike strolls forward"

kitty = Cat("Kitty")
print(kitty.walk())  # Expected: "Kitty saunters forward"

flash = Cheetah("Flash")
print(flash.walk())  # Expected: "Flash runs forward"

byron = Noble("Byron", "Lord")
print(byron.walk())  # "Lord Byron struts forward"
print(byron.name)    # "Byron"
print(byron.title)   # "Lord"    