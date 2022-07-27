#!/usr/bin/python3
"""defines the Square class"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """describe a square object with attribute size"""

    def __init__(self, size):
        """instantiate a square class"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """return the area of the square"""
        return self.__size ** 2

    def __str__(self):
        """return an instance string"""
        return f"[Square] {self.__size}/{self.__size}"
