"""
Consider the following class that represents 2D vectors:

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Vector({self.x}, {self.y})'

print(Vector(3, 2) + Vector(5, 12))   # Vector(8, 14)
print(Vector(5, 12) - Vector(3, 2))   # Vector(2, 10)
print(Vector(5, 12) * 2)              # Vector(10, 24)
print(3 * Vector(5, 12))              # Vector(15, 36)

my_vector = Vector(5, 7)
my_vector += Vector(3, 9)
print(my_vector)                      # Vector(8, 16)

my_vector -= Vector(1, 7)
print(my_vector)                      # Vector(7, 9)

print(Vector(3, 2) + 5)
# TypeError: unsupported operand type(s) for +: 'Vector'
# and 'int'
The following arithmetic operators need to be defined for Vector objects:

Addition: Add two Vectors:

Vector(a, b) + Vector(c, d) -> Vector(a + c, b + d)
Subtraction: Subtract one Vector from another:

Vector(a, b) - Vector(c, d) -> Vector(a - c, b - d)
Multiplication: Multiply a Vector by an integer:

Vector(a, b) * c -> Vector(a * c, b * c)
c * Vector(a, b) -> Vector(a * c, b * c)
"""
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Vector({self.x}, {self.y})'
    
    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x + other.x, self.y + other.y)
    
    def __iadd__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        
        self.x += other.x
        self.y += other.y
        return self
    
    def __sub__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x - other.x, self.y - other.y)
    
    def __isub__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        
        self.x -= other.x
        self.y -= other.y
        return self
    
    def __mul__(self, multiplier):
        if not isinstance(multiplier, int):
            return NotImplemented
        return Vector(self.x * multiplier, self.y * multiplier)
    
    def __rmul__(self, multiplier):
        if not isinstance(multiplier, int):
            return NotImplemented
        return Vector(self.x * multiplier, self.y * multiplier)

print(Vector(3, 2) + Vector(5, 12))   # Vector(8, 14)
print(Vector(5, 12) - Vector(3, 2))   # Vector(2, 10)
print(Vector(5, 12) * 2)              # Vector(10, 24)
print(3 * Vector(5, 12))              # Vector(15, 36)

my_vector = Vector(5, 7)
my_vector += Vector(3, 9)
print(my_vector)                      # Vector(8, 16)

my_vector -= Vector(1, 7)
print(my_vector)                      # Vector(7, 9)

print(Vector(3, 2) + 5)
# TypeError: unsupported operand type(s) for +: 'Vector'
# and 'int'