#!/usr/bin/python3
"""defines an append_write function"""


def append_write(filename="", text=""):
    """append text at the end of a file
    return the number of written character"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
