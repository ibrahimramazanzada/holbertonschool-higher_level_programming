#!/usr/bin/python3
"""This is a simple module to do smth"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Class that defines a square"""
    def __init__(self, size):
        """Method that initializes the square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
