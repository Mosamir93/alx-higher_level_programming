#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id
"""
from urllib import request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    with request.urlopen(url) as res:
        id = res.headers.get('X-Request-Id')

    print(id)
