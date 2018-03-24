import requests

base_url = 'https://api.github.com/'


def read_users(user, password, index=0):
    path = 'users?since={}'.format(index)
    data = requests.get(base_url + path, auth=(user, password))
    return data.json()
