#!/usr/bin/python3
"""This module defines a class Square that"""
class Square:
    """Class Square that defines a square with a private instance attribute size."""
    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square with size and position."""
        self.size = size
        self.position = position
    @property
    def position(self):
        """Get the value of the private instance attribute position."""
        return self.__position
    @position.setter
    def position(self, value):
        """Set the value of the private instance attribute position."""
        if (not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(num, int) for num in value) or
            not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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

    def my_print(self):
        """Print the square with the character #."""
        if self.__size == 0:
            print()
        else:
            print("\n" * self.__position[1], end="")
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
