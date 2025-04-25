"""
Using decorators, add getter and setter methods to your Car class so you can view and change the color of your car. You should also add getter methods that let you view but not modify the car's model and year. Don't forget to write some tests.
"""
class Car:
    def __init__(self, model, year, color):
        self._model = model
        self._year = year
        self._color = color
        self._speed = 0

    # Color getter and setter
    @property
    def color(self):
        return self._color
    @color.setter
    def color(self, color):
        if not isinstance(color, str):
            raise TypeError('Name must be a string')
        self._color = color

    # Model getter
    @property
    def model(self):
        return self._model
    
    # Year getter
    @property
    def year(self):
        return self._year  

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
print(pontiac.color)
print(pontiac.model)
print(pontiac.year)
pontiac.color = 'navy'
print(pontiac.color)        