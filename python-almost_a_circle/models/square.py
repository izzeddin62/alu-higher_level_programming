#!/usr/bin/python3
"""Square class module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """defines square instances"""

    def __init__(self, size, x=0, y=0, id=None):
        """instantiate a square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """return a square string"""
        return "[Square] ({}) {}/{} - {}".format(
                                                 self.id,
                                                 self.x,
                                                 self.y,
                                                 self.width)
