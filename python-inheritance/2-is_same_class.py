#!/usr/bin/python3
"""defines the is_same_class function"""


def is_same_class(obj, a_class):
    """check if a obj is an instance of a class
    Args:
        obj
        a_class
    """
    return type(obj) == a_class
