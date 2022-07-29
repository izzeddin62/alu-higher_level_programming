#!/usr/bin/python3
"""defines find_peak function"""


def find_peak(list_of_integers):
    """return a peak element"""
    r = len(list_of_integers) - 1
    l = 0
    while l < r:
        mid = l + ((r - l) // 2)
        if(list_of_integers[mid] < list_of_integers[mid + 1]):
            l = mid + 1
        else:
            r = mid
    return r
