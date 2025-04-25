"""
Add a method to the Car class that lets you spray paint the car a specific color. Don't use a setter method for this. Instead, create a method whose name accurately describes what it does. Don't forget to test your code.
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
            raise TypeError('Name must be a string!')
        self._color = color

    # Model getter
    @property
    def model(self):
        return self._model
    
    # Year getter
    @property
    def year(self):
        return self._year
    
    def spray_paint(self, color):
        if not isinstance(color, str):
            raise TypeError('Color should be a string!')
        self._color = color

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
# pontiac.spray_paint(123)
pontiac.spray_paint('navy')
print(pontiac.color)