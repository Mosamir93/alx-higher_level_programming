#!/usr/bin/python3
"""Json write module."""
import json


def save_to_json_file(my_obj, filename):
    """Function definition."""
    with open(filename, mode="w") as file:
        try:
            json.dump(my_obj, filename)
        except TypeError:
            pass
