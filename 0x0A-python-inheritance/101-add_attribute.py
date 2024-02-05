#!/usr/bin/python3
"""Checks if adding an attribute is possible."""


def add_attribute(obj, attribute, value):
    """Function definition."""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)
