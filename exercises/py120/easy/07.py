"""
Refactoring Vehicles
Consider the following classes:

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def get_wheels(self):
        return 4

    def info(self):
        return f"{self.make} {self.model}"

class Motorcycle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def get_wheels(self):
        return 2

    def info(self):
        return f"{self.make} {self.model}"

class Truck:
    def __init__(self, make, model, payload):
        self.make = make
        self.model = model
        self.payload = payload

    def get_wheels(self):
        return 6

    def info(self):
        return f"{self.make} {self.model}"
Refactor these classes so they all use a common superclass, and inherit behavior as needed.
"""
class Vehicle:
    def __init__(self, make, model, wheels=None):
        self.make = make
        self.model = model
        self.wheels = wheels

    def info(self):
        return f"{self.make} {self.model}"
    
    def get_wheels(self):
        return self.wheels

class Car(Vehicle):
    def __init__(self, make, model):
        super().__init__(make, model, 4)

class Motorcycle:
    def __init__(self, make, model):
        super().__init__(make, model, 2)

class Truck:
    def __init__(self, make, model, payload):
        super().__init__(make, model, 6)
        self.payload = payload