#!/usr/bin/python3
"""defines Square class"""


class Square:
    """It represents a square"""
    def __init__(self, size=0):
        """set the square size

        Args:
            size (int, optional): the square size measure
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """returns the area of the square"""
        return self.__size ** 2
