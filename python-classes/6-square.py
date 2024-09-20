#!/usr/bin/python3
"""Shebang line indicating the interpreter for the script."""


class Square:
    """A class that defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        """Initiializes a new square instance"""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Getter for the value of position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for the value of position"""
        if not (isinstance(value, tuple) and len(value) == 2 and
                all(isinstance(num, int) and num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates the area of the square"""
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print("")
            return

        for _ in range(self.__position[1]):
            print("")

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
