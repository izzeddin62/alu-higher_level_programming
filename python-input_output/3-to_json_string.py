#!/usr/bin/python3
"""defines to_json_string function"""
import json


def to_json_string(my_obj):
    """returns the json representation of an object"""
    return json.dumps(my_obj)
