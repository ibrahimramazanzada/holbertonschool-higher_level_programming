""""This module really does smth"""
from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """Abstract class for shapes"""

    @abstractmethod
    def area(self):
        """Calculate area of shape"""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate perimeter of shape"""
        pass


class Circle(Shape):
    """Circle shape"""

    def __init__(self, radius):
        """Initialize circle with radius"""
        self.radius = radius

    def area(self):
        """Calculate area of circle"""
        return pi * self.radius ** 2

    def perimeter(self):
        """Calculate perimeter of circle"""
        return 2 * pi * self.radius


class Rectangle(Shape):
    """Rectangle shape"""

    def __init__(self, width, height):
        """Initialize rectangle with width and height"""
        self.width = width
        self.height = height

    def area(self):
        """Calculate area of rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Calculate perimeter of rectangle"""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print area and perimeter of shape"""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")

circle = Circle(radius=5)
rectangle = Rectangle(width=4, height=7)

shape_info(circle)
shape_info(rectangle)
