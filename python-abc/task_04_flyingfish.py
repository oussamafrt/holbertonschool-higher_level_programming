#!/usr/bin/python3
"""Shebang line indicating the interpreter for the script."""


class Fish:
    """Defines a class"""
    def swim(self):
        """defines swim method"""
        print("The fish is swimming")

    def habitat(self):
        """fenies habitat method"""
        print("The fish lives in water")


class Bird:
    """defines a class"""
    def fly(self):
        """defines fly method"""
        print("The bird is flying")

    def habitat(self):
        """defines habitats method"""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """defines a class"""
    def fly(self):
        print("The flying fish is soaring!")

    def swim(self):
        print("The flying fish is swimming!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")
