#!/bin/bash
#a Bash script that sends a request to a URL passed as an argument, and displays only the status code of the response.
curl -sd "@$2" -H "Content-Type: application/json" "$1"
