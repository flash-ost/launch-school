"""
Question 2
Building on the prior question, we now must also track a basic motorboat. A motorboat has a single propeller and hull, but otherwise behaves similar to a catamaran. Therefore, creators of Motorboat instances don't need to specify number of hulls or propellers. How would you modify the vehicles code to incorporate a new Motorboat class?
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

class Watercraft(FuelMixin):
    def __init__(self,
                number_propellers,
                number_hulls,
                kilometers_per_liter,
                liters_of_fuel_capacity):
        self.propellers = number_propellers
        self.hulls = number_hulls
        self.set_fuel_efficiency(kilometers_per_liter)
        self.set_fuel_capacity(liters_of_fuel_capacity)


class Catamaran(Watercraft):
    pass

class Motorboat(Watercraft):
    def __init__(self,
                kilometers_per_liter,
                liters_of_fuel_capacity):
        super().__init__(1, 1, kilometers_per_liter, liters_of_fuel_capacity)