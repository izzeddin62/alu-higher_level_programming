#!/usr/bin/python3
"""fetch data, get the status of a website using url and display the statu"""
import urllib.request


"""send a get request"""
if __name__ == "__main__":
    """use urllib.request to send an request to the url"""
    with urllib.request.urlopen("https://intranet.hbtn.io/status") as res:
        body = res.read()
        print("Body response:")
        print(f"- type: {type(body)}")
        print(f"- content: {body}")
        print(f"- utf8 content: {body.decode('utf-8')}")
