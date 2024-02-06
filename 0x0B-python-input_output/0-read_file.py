#!/usr/bin/python3
"""Read file module."""


def read_file(filename=""):
    """Function definition."""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
