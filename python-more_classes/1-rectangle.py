#!/usr/bin/python3
"""This is a simple module that defines a Rectangle class"""


class Rectangle:
    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle instance."""
        self.width = width
        self.height = height
    """Represents a rectangle shape."""
    @property
    def width(self):
        """The width of the rectangle."""
        return self.__width
    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        if value < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(value, (int)):
            raise TypeError("width must be an integer")
        self.__width = value
    @property
    def height(self):
        """The height of the rectangle."""
        return self.__height
    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        if value < 0:
            raise ValueError("height must be >= 0")
        if not isinstance(value, (int)):
            raise TypeError("height must be an integer")
        self.__height = value
