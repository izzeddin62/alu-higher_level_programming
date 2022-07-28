#!/usr/bin/python3
"""defines a pascal triangle function"""


def pascal_triangle(n):
    """returns the pascal triangle"""
    if n <= 0:
        return []
    result = []
    for i in range(n):
        if i == 0:
            result.append([1])
        else:
            res = []
            new_list = result[i - 1][:]
            new_list.insert(0, 0)
            new_list.append(0)
            j = 0
            while j < len(new_list) - 1:
                res.append(new_list[j] + new_list[j + 1])
                j += 1
            result.append(res)
    return result
