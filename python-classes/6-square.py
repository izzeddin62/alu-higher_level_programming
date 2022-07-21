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
            is_position = type(position) != tuple or len(position) != 2
            type_check = type(position[0]) != int or type(position[1]) != int
            position_check = position[0] < 0 or position[1] < 0
            if is_position or type_check or position_check:
                first_part = "position must be a tuple"
                returned_error = f"{first_part} of 2 positive integers"
                raise TypeError(returned_error)
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
            printed_square = ""
            while i < self.__size:
                position = " " * self.__position[0]
                size = "#" * self.__size
                printed_square += position + size + "\n"
                i += 1
            if(self.__position[1]) > 0:
                for i in range(self.__position[1]):
                    print("")
            print(printed_square, end="")
