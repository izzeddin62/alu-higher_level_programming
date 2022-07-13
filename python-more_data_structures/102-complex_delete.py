#!/sur/bin/python3
def complex_delete(a_dictionary, value):
    for i in sorted(a_dictionary):
        if a_dictionary[i] == value:
            a_dictionary.pop(i)
    return a_dictionary
