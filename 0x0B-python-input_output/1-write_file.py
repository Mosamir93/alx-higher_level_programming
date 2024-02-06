#!/usr/bin/python3
"""Write module."""


def write_file(filename="", text=""):
    """Function definition."""
    with open(filename, mode="w", encoding="utf-8") as file:
       return file.write(text)
