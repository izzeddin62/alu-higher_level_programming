#!/usr/bin/python3
"""defines the LockedClass

   the LockedClass is a class that only allows attribute first_name
"""


class LockedClass:
    """LockedClass class with only first_name attribute"""
    __slots__ = "first_name"
