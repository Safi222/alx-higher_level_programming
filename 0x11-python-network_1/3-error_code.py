#!/usr/bin/python3

"""
Take a URL, send a request to the URL
and display the body of the response (decoded in utf-8)
If there is an HTTPError display the error code
"""


if __name__ == "__main__":
    import urllib.request
    from urllib.error import HTTPError
    from sys import argv

    try:
        with urllib.request.urlopen(argv[1]) as response:
            body = response.read()
            print(body.decode('utf-8'))
    except HTTPError as e:
        print(f'Error code: {e.code}')
