#!/usr/bin/python3
"""Shebang line indicating the interpreter for the script."""


class Square:
    """A class that defines a square"""
    def __init__(self, size=0):
        """Initiializes a new square instance"""
        self.size = size

    @property
    def size(self):
        """Getter for the value of size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for the value of size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates the area of the square"""
        return self.__size * self.__size

    def my_print(self):
        """Prints a square with the character '#' based on the size of the square"""
        if self.__size == 0:
            print("")
        for index in range(self.__size):
            print("#" * self.__size)
