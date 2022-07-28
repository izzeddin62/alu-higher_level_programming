#!/usr/bin/python3
"""defines from_json_string function"""
import json


def from_json_string(my_str):
    """return the actual object from a json string"""
    return json.loads(my_str)
