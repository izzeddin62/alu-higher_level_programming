#!/usr/bin/python3
"""a script that save a python list in a file"""
import sys
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

filename = "add_item.json"
try:
    file_list = load_from_json_file(filename)
    save_to_json_file(file_list + sys.argv[1:], filename)
except FileNotFoundError:
    save_to_json_file(sys.argv[1:], filename)
