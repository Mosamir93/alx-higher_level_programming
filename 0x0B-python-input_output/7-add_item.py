#!/usr/bin/python3
"""Adds arguments to a python list."""
import sys
from os import path
save_to_json_file = __import__(5-save_to_json_file.py).save_to_json_file
load_from_json_file = __import__(6-load_from_json_file.py).load_from_json_file


file = "add_item.json"
list = []
if path.exists(file):
    list = load_from_json_file(file)
list.extend(sys.argv[1:])
save_to_json_file(list, file)
