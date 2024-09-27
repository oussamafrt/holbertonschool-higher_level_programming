#!/usr/bin/python3
"""Shebang line indicating the interpreter for the script."""


class CountedIterator:
    """Defines a class"""
    def __init__(self, data):
        """Defines the iterator"""
        self.data = data
        self.index = 0
        self.count = 0

    def __iter__(self):
        """Return the iterator object itself"""
        return self

    def __next__(self):
        """Returns the next item in the data"""
        if self.index >= len(self.data):
            raise StopIteration
        self.index += 1
        self.count += 1
        return self.data[self.index - 1]

    def get_count(self):
        """method to retrieve and print the number of items"""
        return self.count
