#!/usr/bin/python3
def uppercase(str):
    new = ""
    for char in str:
        if 'a' <= char <= 'z':
            upper = chr(ord(char) - 32)
            new += upper
        else:
            new += char
    print("{}".format(new))
