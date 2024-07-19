#!/usr/bin/python3

"""
Take a URL, send a request to the URL
and display the body of the response (decoded in utf-8)
If there is an HTTPError display the error code
"""


if __name__ == "__main__":
    import requests
    from sys import argv

    payload = {'q': ''}
    url = 'http://0.0.0.0:5000/search_user'
    if len(argv) > 1:
        payload['q'] = argv[1]
    r = requests.post(url, data=payload)
    try:
        json = r.json()
        if (len(json) > 0):
            print(f"[{json['id']}] {json['name']}")
        else:
            print("No result")
    except ValueError:
        print('Not a valid JSON')
