#!/usr/bin/python3
def uppercase(c):
    for i in c:
        if(ord(i) > 90):
            print('{}'.format(chr(ord(i) - 32)), end='')
        else:
            print('{}'.format(i), end='')
    else:
        print('')
