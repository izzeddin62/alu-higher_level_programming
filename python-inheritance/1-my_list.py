#!/usr/bin/python3
"""defines MyList class"""


class MyList(list):
    """inherit list class"""
    def print_sorted(self):
        """print the sorted list"""
        print(sorted(self))
