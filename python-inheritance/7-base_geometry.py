#!/usr/bin/python3
"""defines the BaseGeometry"""


class BaseGeometry:
    """create BaseGeometry
       base geometry instance contains
       public area and integer_validator method
    """

    def area(self):
        """return the area of geometry"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate integer"""
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
