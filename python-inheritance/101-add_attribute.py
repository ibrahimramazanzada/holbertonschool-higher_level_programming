#!/usr/bin/python3
"""This module really does smth"""


def add_attribute(obj, name, value):
    """Adds an attribute to an object"""
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
