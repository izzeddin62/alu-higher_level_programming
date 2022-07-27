#!/usr/bin/python3
"""defines add_attribute function"""


def add_attribute(obj, name, value):
    """adds an attribute to an object if it is possible"""

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, value)
