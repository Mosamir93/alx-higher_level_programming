#!/bin/bash
#A script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
if [ "$#" -ne 1 ]; then
    echo "Usage: 0-body_size.sh <URL>"
    exit 1
fi

url=$1
response=$(curl -sI "$url" | grep -i Content-Length | awk '{print $2}')
echo "$response"
