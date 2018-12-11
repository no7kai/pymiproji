import requests
import json
import sys

base_url = 'https://api.github.com/'
headers = {'Content-Type': 'application/json',
           'User-Agent': 'no7kai',
           'Accept': 'application/vnd.github.v3+json'}


def get_repos(username):
	api_url = '{}users/{}/repos'.format(base_url, username)
	r = requests.get(api_url, headers=headers)
	if r.status_code == 200:
		return r.json()
	else:
		print(('[!] Error HTTP {}'.format(r.status_code)))
		return None

username = sys.argv[1]
data = get_repos(username)

if data is not None:
    for repo in data:
        print(repo['name'])
else:
	print('No repo list found!')