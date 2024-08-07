#!/usr/bin/python3

"""
Print the last 10 commits of a repository
"""


if __name__ == "__main__":
    import requests
    from sys import argv

    url = f'https://api.github.com/repos/{argv[2]}/{argv[1]}/commits'
    payload = {'per_page': 10}
    r = requests.get(url, data=payload)
    try:
        json = r.json()
        for i in range(10):
            commit = json[i]
            sha = commit.get('sha')
            user = commit.get('commit').get('author').get('name')
            print(f"{sha}: {user}")
    except (ValueError, IndexError):
        pass
