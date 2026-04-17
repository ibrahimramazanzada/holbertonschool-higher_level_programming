#!/usr/bin/python3
"""This module really does smth"""


class MyInt(int):
    """MyInt class"""

    def __eq__(self, value):
        """roller degisti"""
        return super().__ne__(value)

    def __ne__(self, value):
        """ibre tersine dondu"""
        return super().__eq__(value)
