#!/usr/bin/python3
"""This is a simple module to do smth"""


class BaseGeometry:
    """Base class for all geometrical shapes"""
    def area(self):
        """Method that raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method that validates value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Class that defines a rectangle"""
    def __init__(self, width, height):
        """Method that initializes the rectangle"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
