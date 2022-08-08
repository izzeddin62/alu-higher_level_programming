#!/usr/bin/python3
"""square module"""


def print_square(size):
    """print the square with #"""
    if type(size) != int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        return
    else:
        i = 0
        while i < size:
            print("#" * size)
            i += 1
