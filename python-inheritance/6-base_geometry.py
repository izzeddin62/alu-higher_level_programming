#!/usr/bin/python3
"""defines the BaseGeometry"""


class BaseGeometry:
    """create BaseGeometry instance with public area method"""
    def area(self):
        """return the area of geometry"""
        raise Exception("area() is not implemented")
