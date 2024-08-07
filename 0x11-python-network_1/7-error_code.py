#!/usr/bin/python3

"""
Take a URL, send a request to the URL
and display the body of the response (decoded in utf-8)
If there is an HTTPError display the error code
"""


if __name__ == "__main__":
    import requests
    from sys import argv

    r = requests.get(argv[1])
    if (r.status_code >= 400):
        print(f'Error code: {r.status_code}')
    else:
        print(r.text)
