#!/usr/bin/python3
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 'division by 0'
    except TypeError:
        return "wrong type"


def list_division(my_list_1, my_list_2, list_length):
    new_list = list(map(safe_divide, my_list_1, my_list_2))
    try:
        i = 0
        while i < list_length:
            try:
                if type(new_list[i]) == str:
                    print("{}".format(new_list[i]))
                i += 1
            except IndexError:
                print("out of range")
                break
    finally:
        returned_list = list(
            map(lambda x: 0 if type(x) == str else x, new_list))
        x = len(returned_list) - 1
        while x < max(len(my_list_1), len(my_list_2)) - 1:
            returned_list.append(0)
            x += 1
        return returned_list
