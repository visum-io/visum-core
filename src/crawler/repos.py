import requests

base_url = 'https://api.github.com/'


def read_repositories(user, password, index=0):
    path = 'repositories?since={}'.format(index)
    result = requests.get(base_url + path, auth=(user, password))
    repos_list = result.json()
    for repo in repos_list:
        languages = requests.get(repo['languages_url'], auth=(user, password))
        repo['languages'] = languages.json()
    return repos_list


