#!/usr/bin/python3
"""defines class_to_json function"""


def class_to_json(obj):
    """returns the dict of an object attribute"""
    return vars(obj)
