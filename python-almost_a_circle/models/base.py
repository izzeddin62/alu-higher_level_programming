#!/usr/bin/python3
"""Base class module"""


class Base:
    """create base instant"""
    __nb_objects = 0
    def __init__(self, id=None):
        if type(id) != None:
            self.id = id
        else:
            __nb_objects += 1
            self.id = __nb_objects
