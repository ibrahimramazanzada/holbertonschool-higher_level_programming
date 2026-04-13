"""This module really does smth"""


class VerboseList(list):
    """This class is a list, but with some extra features"""

    def append(self, object):
        """Appends an object to the list with a message"""
        print(f"Added [{object}] to the list")
        return super().append(object)

    def extend(self, iterable):
        """Extends the list with an iterable and prints a message"""
        print(f"Extended the list with [{len(iterable)}] items")
        return super().extend(iterable)

    def remove(self, value):
        """Removes an object from the list with a message"""
        print(f"Removed [{value}] from the list")
        return super().remove(value)

    def pop(self, index=-1):
        """Pops an object from the list with a message"""
        value = super().pop(index)
        print(f"Popped [{value}] from the list")
        return value
