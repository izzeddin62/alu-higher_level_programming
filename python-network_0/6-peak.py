#!/usr/bin/python3
"""defines find_peak function"""


def find_peak(list_of_integers):
    """return a peak element"""
    right = len(list_of_integers) - 1
    left = 0
    while left < right:
        mid = (left + ((right - left) // 2))
        if(list_of_integers[mid] < list_of_integers[mid + 1]):
            left = mid + 1
        else:
            right = mid
    return list_of_integers[right]
