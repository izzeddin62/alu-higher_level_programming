#!/usr/bin/python3
"""defines a Student class"""


class Student:
    """describe a student instance"""

    def __init__(self,  first_name, last_name, age):
        """initialize a student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """return a dict representation of the instance"""
        json_rep = dict(vars(self))
        if type(attrs) == list:
            for i in list(json_rep):
                if i not in attrs:
                    json_rep.pop(i, None)
        return json_rep

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance with json"""
        for i in list(json):
            setattr(self, i, json[i])
