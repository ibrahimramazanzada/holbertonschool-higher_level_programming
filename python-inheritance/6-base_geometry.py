#!/usr/bin/python3
"""This is a simple module to do smth"""


class BaseGeometry:
    """Base class for all geometrical shapes"""
    def area(self):
        """Method that raises an exception"""
        raise Exception("area() is not implemented")
