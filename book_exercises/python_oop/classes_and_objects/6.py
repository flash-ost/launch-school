class Car:
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color
        self.speed = 0

    @staticmethod
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