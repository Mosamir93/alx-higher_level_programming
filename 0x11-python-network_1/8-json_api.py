#!/usr/bin/python3
"""
Takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 2:
        q = sys.argv[1]
    else:
        q = ""

    res = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        j_res = res.json()
        if j_res == {}:
            print("No result")
        else:
            print(f"[{j_res.get('id')}] {j_res.get('name')}")
    except ValueError:
        print("Not a valid JSON")
