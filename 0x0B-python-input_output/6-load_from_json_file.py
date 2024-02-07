#!/usr/bin/python3
"""From json file to pyobject."""
import json


def load_from_json_file(filename):
    """Function definition."""
    with open(filename) as file:
        return json.load(file)
