""""This module really does smth"""


class CountedIterator:
    """An iterator that counts how many items it has returned."""
    def __init__(self, iterable):
        """Initialize the CountedIterator with an iterable."""
        self.iterator = iter(iterable)
        self.counter = 0

    def __iter__(self):
        """Return the iterator object itself."""
        return self

    def __next__(self):
        """Return the next item from the iterator"""
        item = next(self.iterator)
        self.counter += 1
        return item

    def get_count(self):
        """Return the number of items that have been returned."""
        return self.counter
