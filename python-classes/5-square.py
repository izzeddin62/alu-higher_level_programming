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

    def my_print(self):
        """shows the square area on the stdout using #"""
        i = 0
        if self.__size == 0:
            print("")
        else:
            while i < self.__size:
                print("#" * self.__size)
                i += 1
