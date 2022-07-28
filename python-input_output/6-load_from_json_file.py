#!/usr/bin/python3
"""defines load_from_json_file function"""
import json


def load_from_json_file(filename):
    """returns an object from a json file"""
    return json.loads(filename)
