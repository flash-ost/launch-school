"""
Add a class method to your Car class that calculates and prints any car's average gas mileage (miles per gallon). You can compute the mileage by dividing the distance traveled (in miles) by the fuel burned (in gallons).
"""
class Car:
    @classmethod
    def avg_gas_mileage(cls, distance, fuel_burned):
        for el in (distance, fuel_burned):
            if not isinstance(el, float) and not isinstance(el, int):
                raise TypeError('Both arguments should be of type floau or int!')
            if el <= 0:
                raise ValueError('Both arguments should be greater than zero')
        mileage = distance / fuel_burned
        print(f'Average mileage: {mileage} miles per gallon')

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
pontiac.avg_gas_mileage(200, 50)