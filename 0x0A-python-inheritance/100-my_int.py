#!/usr/bin/python3
"""Myint class module."""


class MyInt(int):
    """Class definition."""
    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
