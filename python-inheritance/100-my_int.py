#!/usr/bin/python3
"""defines the MyInt class"""


class MyInt(int):
    """describe myint instance that inverse the == and !== operation"""

    def __eq__(self, value):
        """return false if the value are not equal"""
        return super().__ne__(value)

    def __ne__(self, value):
        """return true if the value and self are equal"""
        return super().__eq__(value)
