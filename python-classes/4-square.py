#!/usr/bin/python3
"""This module defines a Square class with a private instance attribute size."""


class Square:
    """Class Square that defines a square with a private instance attribute size."""

    def __init__(self, size=0):
        """Initialize the Square instance with a private instance attribute size."""
        if not isinstance(size, (int)):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size ** 2

    @property
    def size(self):
        """Get the value of the private instance attribute size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the value of the private instance attribute size."""
        if not isinstance(value, (int)):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
