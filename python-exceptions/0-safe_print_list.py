#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        i = 0
        list_string = ""
        while i <= x - 1:
            list_string += f"{my_list[i]}"
            i += 1
        print("{}".format(list_string))
        return i
    except IndexError:
        print("{}".format(list_string))
        return i
