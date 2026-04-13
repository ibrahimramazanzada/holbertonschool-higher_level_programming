"""This module really does smth"""


class SwimMixin:
    """This mixin allows to swim"""

    def swim(self):
        """Swim method"""
        print("The creature swims!")

class FlyMixin:
    """This mixin allows to fly"""

    def fly(self):
        """Fly method"""
        print("The creature flies!")

class Dragon(SwimMixin, FlyMixin):
    """This class represents a dragon"""

    def roar(self):
        """Roar method"""
        print("The dragon roars!")
