#!/usr/bin/python3
"""defines a function write_file"""


def write_file(filename="", text=""):
    """write in a file and return the added characters number"""
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
