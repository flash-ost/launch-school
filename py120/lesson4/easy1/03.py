"""
Question 3
If we have a Car class and a Truck class and we want to be able to go_fast, how can we add the ability for them to go_fast using the mix-in SpeedMixin? How can you check whether your Car or Truck can now go fast?

class SpeedMixin:
    def go_fast(self):
        print(f'I am a super fast {self.__class__.__name__}')

class Car:
    def go_slow(self):
        print('I am safe and driving slow.')

class Truck:
    def go_very_slow(self):
        print('I am a heavy truck and like going very slow.')
"""
# Car and Truck should inherit from SpeedMixin.
# We can then call go_fast method of Car and Truck instances
class SpeedMixin:
    def go_fast(self):
        print(f'I am a super fast {self.__class__.__name__}')

class Car(SpeedMixin):
    def go_slow(self):
        print('I am safe and driving slow.')

class Truck(SpeedMixin):
    def go_very_slow(self):
        print('I am a heavy truck and like going very slow.')

car = Car()
truck = Truck()
car.go_fast()
truck.go_fast()