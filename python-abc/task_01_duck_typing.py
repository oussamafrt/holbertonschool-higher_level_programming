#!/usr/bin/python3
"""Shebang line indicating the interpreter for the script."""


from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Define the abstract class Shape"""
    @abstractmethod
    def area(self):
        """Calculate the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate the perimeter of the shape."""
        pass


class Circle(Shape):
    """Define the Circle class"""
    def __init__(self, radius):
        self.radius = abs(radius)

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Define the Rectangle class"""
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Define a function that prints the area and perimeter of a shape"""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))