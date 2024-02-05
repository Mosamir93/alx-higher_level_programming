#!/usr/bin/python3
"""My list class that inherits from list class."""


class MyList(list):
    """Mylist class definition."""
    def print_sorted(self):
        print(sorted(self))
