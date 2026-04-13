"""This module really does smth"""


class Fish:
    """This class is for fish"""

    def habitat(self):
        """This method is for the fish's habitat"""
        print("The fish lives in water")

    def swim(self):
        """This method is for swimming"""
        print("The fish is swimming")


class Bird():
    """This function is for birds"""
    def habitat():
        """This method is for the bird's habitat"""
        print("The bird lives in the sky")

    def fly():
        """This method is for flying"""
        print("The bird is flying")


class FlyingFish(Fish, Bird):
    """This class is for flying fish"""

    def fly(self):
        """This method is for flying"""
        print("The flying fish is soaring!")

    def swim(self):
        """This method is for swimming"""
        print("The flying fish is swimming!")

    def habitat(self):
        """This method is for the flying fish's habitat"""
        print("The flying fish lives both in water and the sky!")

