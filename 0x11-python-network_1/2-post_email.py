#!/usr/bin/python3

"""
Take a URL and an email, send a POST request to the
passed URL with the email as a parameter,
and display the body of the response
"""


if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    from sys import argv

    values = {'email': argv[2]}
    data = urllib.parse.urlencode(values).encode('ascii')

    with urllib.request.urlopen(argv[1], data) as response:
        body = response.read()
        print(body.decode('utf-8'))
