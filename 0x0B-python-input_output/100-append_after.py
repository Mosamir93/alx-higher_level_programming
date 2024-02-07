#!/usr/bin/python3
"""Append after module."""


def append_after(filename="", search_string="", new_string=""):
    """Function definition."""
    lines_to_append = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            lines_to_append.append(line)
            if search_string in line:
                lines_to_append.append(new_string)

    with open(filename, 'w') as file:
        file.writelines(lines_to_append)
