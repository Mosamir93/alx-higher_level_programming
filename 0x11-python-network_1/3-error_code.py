#!/usr/bin/python3
"""
 takes in a URL, sends a request to the URL and
 displays the body of the response (decoded in utf-8)
"""
from urllib import request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with request.urlopen(url) as res:
            print(res.read().decode('utf-8'))
    except Exception as e:
        print(f"Error code: {e}")
