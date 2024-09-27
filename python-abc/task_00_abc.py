#!/usr/bin/python3
"""Shebang line indicating the interpreter for the script."""


from abc import ABC, abstractmethod


class Animal(ABC):
    """Define the abstract class"""
    @abstractmethod
    def sound(self):
        """Abstract method for sound."""
        pass

class Dog(Animal):
    """Define the Dog class inheriting from Animal"""
    def sound(self):
        return "Bark"

class Cat(Animal):
    """Define the Cat class inheriting from Animal"""
    def sound(self):
        return "Meow"
