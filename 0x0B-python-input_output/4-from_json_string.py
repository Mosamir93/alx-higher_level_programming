#!/usr/bin/python3
"""From json to pyobject."""
import json


def from_json_string(my_str):
    """Function definition."""
    return json.loads(my_str)
