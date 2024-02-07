#!/usr/bin/python3
"""Append module."""


def write_file(filename="", text=""):
    """Function definition."""
    with open(filename, mode="a", encoding="utf-8") as file:
        return file.write(text)
