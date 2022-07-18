#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        i = 0
        list_string = ""
        while i <= x - 1:
            try:
                list_string += "{:d}".format(my_list[i])
                i += 1
            except (TypeError, ValueError):
                i += 1
                pass
        print(list_string)
        length = 0
        for n in list_string:
            length += 1
        return length
    except IndexError:
        print('{}'.format(list_string), end="")
        raise
