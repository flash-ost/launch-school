"""
Print the method resolution order for cars, trucks, boats, and vehicles as defined in the previous exercise.
"""

class Vehicle:
    vehicles_count = 0

    def __init__(self):
        Vehicle.vehicles_count += 1

    def vehicles():
        return Vehicle.vehicles_count
    
class SignalsMixin():
    def signal_left(self):
        print('Signalling left')

    def signal_right(self):
        print('Signalling right')

    def signal_off(self):
        print('Signal is now off')    

class Car(SignalsMixin, Vehicle):
    pass

class Truck(SignalsMixin, Vehicle):
    pass

class Boat(Vehicle):
    pass

print(Car.mro())
print(Truck.mro())
print(Boat.mro())
print(Vehicle.mro())