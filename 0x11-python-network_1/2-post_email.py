#!/usr/bin/python3
"""
 takes in a URL and an email, sends a POST request to the passed URL
 with the email as a parameter, and displays the body of the response
 (decoded in utf-8)
"""
from urllib import request, parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = parse.urlencode({'email': email}).encode('utf-8')
    with request.urlopen(url, data=data) as res:
        print(res.read().decode('utf-8'))
