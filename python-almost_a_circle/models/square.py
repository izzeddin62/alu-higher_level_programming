#!/usr/bin/python3
"""Square class module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """defines square instances"""

    def __init__(self, size, x=0, y=0, id=None):
        """instantiate a square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.width = value

    def update(self, *args, **kwargs):
        """update square attributes"""
        try:
            if type(args) == tuple and len(args) > 0:
                self.id = args[0]
                self.width = args[1]
                self.height = args[1]
                self.x = args[2]
                self.y = args[3]  
            else:
                try:
                    self.size = kwargs.get('size')
                except Exception:
                    pass
                try:
                   self.x = kwargs.get('x')
                except Exception:
                   pass
                try:
                    y=kwargs.get('y')
                except:
                    pass
                try:
                    self.id = kwargs['id']
                except:
                    pass
        except Exception:
            pass
    def __str__(self):
        """return a square string"""
        return "[Square] ({}) {}/{} - {}".format(
                                                 self.id,
                                                 self.x,
                                                 self.y,
                                                 self.width)
