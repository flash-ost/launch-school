"""
Create a mix-in for the Car and Truck classes from the previous exercise that lets you operate the turn signals: signal left, signal right, and signal off. Use the following code to test your code.

car1.signal_left()       # Signalling left
truck1.signal_right()    # Signalling right
car1.signal_off()        # Signal is now off
truck1.signal_off()      # Signal is now off
boat1.signal_left()
# AttributeError: 'Boat' object has no attribute
# 'signal_left'
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

car1 = Car()
truck1 = Truck()
boat1 = Boat()

car1.signal_left()       # Signalling left
truck1.signal_right()    # Signalling right
car1.signal_off()        # Signal is now off
truck1.signal_off()      # Signal is now off
boat1.signal_left()