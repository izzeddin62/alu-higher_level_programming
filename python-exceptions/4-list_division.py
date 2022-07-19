#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    i = 0
    while i < list_length:
        try:
            new_list.append(my_list_1[i] / my_list_2[i])
            i += 1
        except ZeroDivisionError:
            print("division by 0")
            new_list.append(0)
            i += 1
        except TypeError:
            print("wrong type")
            new_list.append(0)
            i += 1
        except IndexError:
            print("out of range")
            new_list.append(0)
            break
    return new_list
