#!/usr/bin/python3
"""
send a get request to a url provided
handle HttpError and display the error status
"""


import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as res:
            body = res.read()
            print(body.decode("utf-8"))
    except urllib.error.HTTPError as error:
        print(f"Error code: {error.status}")
