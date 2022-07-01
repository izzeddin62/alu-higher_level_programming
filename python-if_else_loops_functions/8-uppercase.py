#!/bin/usr/python3
def uppercase(c):
    for i in c:
        if(ord(i) > 90):
            print(chr(ord(i) - 32), end='')
        else:
            print(i, end='')
    else:
        print('')
