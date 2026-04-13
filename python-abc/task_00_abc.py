""""This module really does smth"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract class for animals"""

    @abstractmethod
    def sound(self):
        """Make sound method"""
        pass


class Dog(Animal):
    """Dog class"""

    def sound(self):
        """Make sound method for dog"""
        return "Bark"
    

class Cat(Animal):
    """Cat class"""

    def sound(self):
        """Make sound method for cat"""
        return "Meow"
