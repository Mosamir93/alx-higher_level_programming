#!/usr/bin/python3
"""Find peak module."""


def find_peak(list_of_integers):
    """A function that finds the peak of the list."""
    if not list_of_integers:
        return None
    high = len(list_of_integers) - 1
    low = 0

    while low < high:
        mid = (low + high) // 2
        if list_of_integers[mid] > list_of_integers[mid + 1]:
            high = mid
        else:
            low = mid + 1
    return list_of_integers[low]
