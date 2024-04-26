#!/usr/bin/python3
"""
Takes your GitHub credentials (username and password)
and uses the GitHub API to display your id.
"""
import requests
import sys

if __name__ == "__main__":
    usr = sys.argv[1]
    passwd = sys.argv[2]
    url = "https://api.github.com/user"

    res = requests.get(url, auth=(usr, passwd))
    if res.ok:
        usr_data = res.json()
        print(usr_data['id'])
    else:
        print(None)
