#!/usr/bin/python3
"""This is a simple module to do smth"""


def inherits_from(obj, a_class):
    """This is a function that does smth."""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
