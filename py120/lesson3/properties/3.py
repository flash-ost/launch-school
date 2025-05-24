"""
Create a Rectangle class with attributes _width and _height. Add properties to get the width and height but to disallow modification after the object is created (i.e., no setters).
"""
class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height
    
rectangle = Rectangle(3, 8)
print(rectangle.width)
print(rectangle.height)
rectangle.width = 5    