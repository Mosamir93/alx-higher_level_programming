#!/usr/bin/python3
def remove_char_at(str, n):
    new = ""
    for i, c in enumerate(str):
        if i != n:
            new += c
    return new
