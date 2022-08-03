#!/usr/bin/python3
"""send a get request to a url provided and handle error"""
import requests
import sys


if __name__ == "__main__":
    try:
        res = requests.get(sys.argv[1])
        print(res.text)
    except requests.exceptions.HTTPError as error:
        print(error)
        print("Error code: {}".format(error.response.status_code))
