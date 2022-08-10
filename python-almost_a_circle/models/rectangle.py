#!/usr/bin/python3
"""rectangle module"""
from models.base import Base


class Rectangle(Base):
    """creates rectangles"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """instantiate a rectangle"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def to_dictionary(self):
        """returns the dictionary representation of the object"""
        return {'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y}

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """returns the area"""
        return self.width * self.height

    def display(self):
        """display the rectangle using #"""
        for i in range(self.y):
            print("")
        for i in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        text = "[Rectangle] ({}) {}/{} - {}/{}".format(
                                                       self.id,
                                                       self.x,
                                                       self.y,
                                                       self.width,
                                                       self.height)
        return text

    def update(self, *args, **kwargs):
        """update all or some rectangle attribute"""
        try:
            if type(args) == tuple and len(args) > 0:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
                return
            try:
                self.id = kwargs['id']
            except Exception:
                pass
            try:
                self.width = kwargs.get('width')
            except Exception:
                pass
            try:
                self.height = kwargs.get('height')
            except Exception:
                pass
            try:
                self.x = kwargs.get('x')
            except Exception:
                pass
            try:
                self.y = kwargs.get('y')
            except Exception:
                pass
        except Exception:
            pass
