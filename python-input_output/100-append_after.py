#!/usr/bin/python3
"""defines the append_after function"""


def append_after(filename="", search_string="", new_string=""):
    """append a new string after a line containing some text
    and save it in a file"""
    new_text = ""
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            new_text += line
            if search_string in line:
                new_text += new_string
    with open(filename, "w", encoding="utf-8") as j:
        j.write(new_text)
