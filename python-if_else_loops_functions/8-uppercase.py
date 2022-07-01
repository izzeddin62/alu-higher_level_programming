#!/usr/bin/python3
def uppercase(c):
    uppercaseword = ''
    for i in c:
        if(ord(i) > 90):
            uppercaseword = uppercaseword + chr(ord(i) - 32)
        else:
            uppercaseword = uppercaseword + i
    print('{}'.format(uppercaseword))
