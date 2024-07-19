#!/usr/bin/python3
"""Fetch https://alx-intranet.hbtn.io/status using requests module"""


if __name__ == "__main__":
    import requests

    url = 'https://alx-intranet.hbtn.io/status'
    r = requests.get(url)
    print("Body response:")
    print(f"\t- type: {r.text.__class__}")
    print(f"\t- content: {r.text}")
