#!/usr/bin/python3
"""Base class module"""


class Base:
    """create base instant"""
    __nb_objects = 0

    def __init__(self, id=None):
        """instantiate base instance"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
