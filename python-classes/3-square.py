#!/usr/bin/python3
"""Shebang line indicating the interpreter for the script."""


class Square:
    """A class that defines a square"""
    def __init__(self, size=0):
        """Initiializes a new square instance"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculates the area of the square"""
        return self.__size * self.__size
