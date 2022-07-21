#!/usr/bin/python3
"""defines Square class"""


class Square:
    """It represents a square, calculate the square area"""
    def __init__(self, size=0, position=(0, 0)):
        """set the square size
        Args:
            size (int, optional)
            position(tuple, optional)
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """get the position attribute"""
        return self.__position

    @position.setter
    def position(self, position):
        """set the position attribute
        Args:
            position (tuple): new position value
        """
        try:
            if type(position) != tuple or len(position) != 2 or type(position[0]) != int or type(position[1]) != int or position[0] < 0 or position[1] < 0:
                raise TypeError("position must be a tuple of 2 positive integers")
            else:
                self.__position = position
        except IndexError:
            raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        """shows the square area on the stdout using #"""
        i = 0
        if self.__size == 0:
            print("")
        else:
            while i < self.__size:
                print("#" * self.__size)
                i += 1
