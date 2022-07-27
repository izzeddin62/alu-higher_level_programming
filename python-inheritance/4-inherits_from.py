#!/usr/bin/python3
"""defines the inherits_from function"""


def inherits_from(obj, a_class):
    """check if a obj is a subclass of a_class
    Args:
        obj
        a_class
    """
    if (type(obj) == a_class):
        return False
    return issubclass(type(obj), a_class)
