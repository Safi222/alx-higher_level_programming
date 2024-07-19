#!/usr/bin/python3

"""
Fetch a url and display the value of
the X-Request-Id variable found
in the header of the response
"""


if __name__ == "__main__":
    import urllib.request
    from sys import argv

    with urllib.request.urlopen(argv[1]) as response:
        x_id = response.headers.get('X-Request-Id')
        print(x_id)
