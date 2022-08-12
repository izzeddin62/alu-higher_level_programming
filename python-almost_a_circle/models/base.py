#!/usr/bin/python3
"""Base class module"""

import json


class Base:
    """create base instant"""
    __nb_objects = 0

    def __init__(self, id=None):
        """instantiate base instance"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """return json representation"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save json to file"""
        dict_list = None
        if list_objs is not None:
            dict_list = [i.to_dictionary() for i in list_objs]
        with open(cls.__name__ + '.json', 'w', encoding='utf-8') as f:
            f.write(Base.to_json_string(dict_list))

    @staticmethod
    def from_json_string(json_string):
        """convert json to list"""
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """create base instance"""
        if cls.__name__ == 'Square':
            shape = cls(1)
        else:
            shape = cls(1, 1)
        shape.update(**dictionary)
        return shape

    @classmethod
    def load_from_file(cls):
        try:
            with open(cls.__name__ + '.json') as f:
                text = f.read()
                return [cls.create(**i) for i in cls.from_json_string(text)]
        except FileNotFoundError:
            return []
