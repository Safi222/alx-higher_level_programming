#!/usr/bin/python3

"""
Authenticate to github and print the
id of the authenticated user
"""


if __name__ == "__main__":
    import requests
    from sys import argv

    url = 'https://api.github.com/user'
    r = requests.get(url, auth=(argv[1], argv[2]))
    try:
        print(r.json().get('id'))
    except ValueError:
        pass
