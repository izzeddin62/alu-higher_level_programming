#!/usr/bin/python3
"""defines a read_file function"""


def read_file(filename=""):
    """print the content of a file"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
