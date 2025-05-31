"""
Question 1
Ben and Alyssa are working on a vehicle management system. So far, they have created classes called Auto and Motorcycle to represent automobiles and motorcycles. After having noticed common information and calculations they were performing for each vehicle type, they decided to break the common behaviors into a separate class called WheeledVehicle. This is what their code looks like so far:

class WheeledVehicle:
    def __init__(self,
                 tire_list,
                 kilometers_per_liter,
                 liters_of_fuel_capacity):
        self.tires = tire_list
        self.fuel_efficiency = kilometers_per_liter
        self.fuel_capacity = liters_of_fuel_capacity

    def tire_pressure(self, tire_index):
        return self.tires[tire_index]

    def inflate_tire(self, tire_index, pressure):
        self.tires[tire_index] = pressure

    def range(self):
        return self.fuel_capacity * self.fuel_efficiency

class Auto(WheeledVehicle):
    def __init__(self):
        # 4 tires with various tire pressures
        super().__init__([30, 30, 32, 32], 50, 25.0)

class Motorcycle(WheeledVehicle):
    def __init__(self):
        # 2 tires with various tire pressures
        super().__init__([20, 20], 80, 8.0)
Now Syl has asked them to incorporate a new type of vehicle into their system: a Catamaran, defined as follows:

class Catamaran:
    def __init__(self,
                number_propellers,
                number_hulls,
                kilometers_per_liter,
                liters_of_fuel_capacity):
        # ... code omitted ...
This new class does not fit well with the object hierarchy defined so far. Catamarans don't have tires. But we still want a common code to track fuel efficiency and range. Modify the class definitions and move code into a mix-in, as necessary, to share code among the Catamaran and the wheeled vehicles.
"""
class FuelMixin:
    def set_fuel_efficiency(self, kilometers_per_liter):
        self.fuel_efficiency = kilometers_per_liter

    def set_fuel_capacity(self, liters_of_fuel_capacity):
        self.fuel_capacity = liters_of_fuel_capacity

    def range(self):
        return self.fuel_capacity * self.fuel_efficiency

class WheeledVehicle(FuelMixin):
    def __init__(self,
                 tire_list,
                 kilometers_per_liter,
                 liters_of_fuel_capacity):
        self.tires = tire_list
        self.set_fuel_efficiency(kilometers_per_liter)
        self.set_fuel_capacity(liters_of_fuel_capacity)

    def tire_pressure(self, tire_index):
        return self.tires[tire_index]

    def inflate_tire(self, tire_index, pressure):
        self.tires[tire_index] = pressure

class Auto(WheeledVehicle):
    def __init__(self):
        # 4 tires with various tire pressures
        super().__init__([30, 30, 32, 32], 50, 25.0)

class Motorcycle(WheeledVehicle):
    def __init__(self):
        # 2 tires with various tire pressures
        super().__init__([20, 20], 80, 8.0)

class Catamaran(FuelMixin):
    def __init__(self,
                number_propellers,
                number_hulls,
                kilometers_per_liter,
                liters_of_fuel_capacity):
        self.propellers = number_propellers
        self.hulls = number_hulls
        self.set_fuel_efficiency(kilometers_per_liter)
        self.set_fuel_capacity(liters_of_fuel_capacity)

auto = Auto()
motorcycle = Motorcycle()
catamaran = Catamaran(2, 2, 1.5, 600)

print(auto.fuel_efficiency)             # 50
print(auto.fuel_capacity)               # 25.0
print(auto.range())                     # 1250.0

print(motorcycle.fuel_efficiency)       # 80
print(motorcycle.fuel_capacity)         # 8.0
print(motorcycle.range())               # 640.0

print(catamaran.fuel_efficiency)        # 1.5
print(catamaran.fuel_capacity)          # 600
print(catamaran.range())                # 900.0        