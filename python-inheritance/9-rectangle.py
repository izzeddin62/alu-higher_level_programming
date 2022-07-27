#!/usr/bin/python3
"""contains the Rectangle class"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """create a rectange"""

    def __init__(self, width, height):
        """instatiate a rectangle object"""
        self.integer_validator("height", height)
        self.integer_validator("width", width)
        self.__height = height
        self.__width = width

    def area(self):
        """return the area of the rectangle"""
        return self.__height * self.__width

    def __str__(self):
        """return the rectangle string"""
        return f"[Rectangle] {self.__width}/{self.__height}"
