#!/usr/bin/python3
"""the script get the status from intranet.hbtn.io"""
import urllib.request


"""send a get request"""
if __name__ = "__main__"
    with urllib.request.urlopen("https://intranet.hbtn.io/status") as res:
        body = res.read()
        print("Body response:")
        print(f"- type: {type(body)}")
        print(f"- content: {body}")
        print(f"- utf8 content: {body.decode('utf-8')}")
