#!/usr/bin/python3
"""the script get the status from intranet.hbtn.io"""

import urllib.request

with urllib.request.urlopen("https://intranet.hbtn.io/status") as res:
    body = res.read()
    print("Body response:")
    print(f"- type: {type(body)}")
    print(f"- content: {body}")
    print(f"- utf8 content: {body.decode('utf-8')}")
