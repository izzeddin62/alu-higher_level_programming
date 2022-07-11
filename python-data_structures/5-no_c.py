#!/usr/bin/python3
def no_c(my_string):
    string_array = []
    for i in range(len(my_string)):
        string_array.append(my_string[i])
    formatted_array = [i for i in string_array if (i != "c" and i != "C")]
    formatted_string = ""
    for i in formatted_array:
        formatted_string = formatted_string + i
    return formatted_string
