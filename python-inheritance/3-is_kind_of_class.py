#!/usr/bin/python3
"""defines the is_kind_of_class function"""


def is_kind_of_class(obj, a_class):
    """check if a obj is an instance of a class or from any class BaseClass
    Args:
        obj
        a_class
    """
    return isinstance(obj, a_class)
