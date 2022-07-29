#!/usr/bin/python3
"""defines the append_after function"""


def append_after(filename="", search_string="", new_string=""):
    """append a new string after a line containing some text
    and save it in a file"""
    new_text = ""
    with open(filename, "r", encoding="utf-8") as f:
        new_text = f.read()
        f.seek(0)
        for line in f:
            print(search_string, line, search_string in line)
            if search_string in line:
                pos = new_text.find(line)
                insert_pos = new_text[:pos + len(line)]
                end_pos = new_text[pos + len(line):]
                new_text = insert_pos + new_string + end_pos
    with open(filename, "w", encoding="utf-8") as j:
        j.write(new_text)
