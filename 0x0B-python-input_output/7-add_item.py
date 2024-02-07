#!/usr/bin/python3
"""Adds arguments to a python list."""
import json
import sys
from os import path
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file


file = "add_item.json"
list = []
if path.exists(file):
    list = load_from_json_file(file)
list.extend(sys.argv[1:])
save_to_json_file(list, file)
