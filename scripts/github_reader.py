import requests

base_url = 'https://api.github.com/'


def read_repositories(index=0):
    path = 'repositories?since={}'.format(index)
    result = requests.get(base_url + path)
    return map(lambda i: i['full_name'], result.json())

