#!/usr/bin/python3
def remove_char_at(str, n):
    copiedstring = ''
    for i in range(len(str)):
        if i != n:
            copiedstring = copiedstring + str[i]
    return copiedstring
