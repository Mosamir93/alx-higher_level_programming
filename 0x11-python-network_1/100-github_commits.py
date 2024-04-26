#!/usr/bin/python3
"""
list 10 commits (from the most recent to oldest) of the repository
“rails” by the user “rails” You must use the GitHub API, here is the
documentation https://developer.github.com/v3/repos/commits/
Print all commits by: `<sha>: <author name>` (one by line)
"""
import requests
import sys

if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"

    res = requests.get(url)
    if res.ok:
        commits = res.json()[:10]
        for commit in commits:
            sha = commit['sha']
            author = commit['commit']['author']['name']
            print(f"{sha}: {author}")
