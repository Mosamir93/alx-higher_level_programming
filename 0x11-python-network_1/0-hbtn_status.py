#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status."""
from urllib import request

url = 'https://alx-intranet.hbtn.io/status'
with request.urlopen(url) as res:
    body = res.read()

print("Body response:")
print("    - type: ", type(body))
print("    - content: ", body)
print("    - utf8 content: ", body.decode('utf-8'))
