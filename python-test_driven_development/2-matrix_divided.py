#!/usr/bin/python3
"""divide matrix module"""


def matrix_divided(matrix, div):
    """divides a matrix elements with a number"""
    if type(div) != int and type(div) != float:
        raise TypeError('div must be a number')
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError('Each row of the matrix must have the same size')
    try:
        return [[round(j / div, 2) for j in i] for i in matrix]
    except TypeError:
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    except ZeroDivisionError:
        raise ZeroDivisionError('division by zero')
