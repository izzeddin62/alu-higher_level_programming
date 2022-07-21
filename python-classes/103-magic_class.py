#!/usr/bin/python3
"""defines the MagicClass class"""
import dis
import math


class MagicClass:
    """creates circle instance"""
    def __init__(self, radius=0):
        if radius is not int and radius is not float:
            raise TypeError("radius must be a number")
        self._MagicClass__radius = radius

    def area(self):
        return (self._MagicClass__radius ** 2) * pi

    def circumference(self):
        return (2 * pi * self._MagicClass__radius)
