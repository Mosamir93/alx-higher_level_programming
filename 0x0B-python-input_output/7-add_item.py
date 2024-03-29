#!/usr/bin/python3
"""Adds arguments to a python list."""


import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

file = "add_item.json"
list = []

try:
    list = load_from_json_file(file)
except Exception:
    save_to_json_file(list, file)

list.extend(sys.argv[1:])
save_to_json_file(list, file)
