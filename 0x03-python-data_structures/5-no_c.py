#!/usr/bin/env python3
def no_c(my_string):
    c_chars = ['c', 'C']
    new = ''.join(char for char in my_string if char not in c_chars)
    return new
