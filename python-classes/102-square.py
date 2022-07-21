#!/usr/bin/python3
"""defines Square class"""


class Square(int):
    """It represents a square"""
    def __new__(cls, size):
        return super().__new__(cls, size ** 2)

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

    @property
    def size(self):
        """get square property"""
        return self.__size

    @size.setter
    def size(self, size):
        """set size property

        Args:
            size (int): represent the new size
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
