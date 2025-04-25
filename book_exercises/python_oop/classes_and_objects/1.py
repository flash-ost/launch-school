"""
Create a Car class that meets these requirements:

Each Car object should have a model, model year, and color provided at instantiation time.
You should have an instance variable that keeps track of the current speed. Initialize it to 0 when you instantiate a new car.
Create instance methods that let you turn the engine on, accelerate, brake, and turn the engine off. Each method should display an appropriate message.
Create a method that prints a message about the car's current speed.
Write some code to test the methods.
"""
class Car:
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color
        self.speed = 0

    def engine_on(self):
        print('Engine\'s on!')

    def engine_off(self):
        self.speed = 0
        print('Engine\'s off!')

    def accelerate(self):
        self.speed += 20
        print(f'You accelerated!')

    def brake(self):
        self.speed = 0 if self.speed < 21 else self.speed - 20
        print(f'You hit the brakes!')

    def current_speed(self):
        print(f'Current speed: {self.speed} km/h')

pontiac = Car('Pontiac', 1990, 'maroon')
pontiac.engine_on()
pontiac.accelerate()
pontiac.accelerate()
pontiac.brake()
pontiac.current_speed()
pontiac.engine_off()