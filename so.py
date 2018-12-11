import requests
import sys

base_url = 'https://api.stackexchange.com/2.2/questions'


def get_faqs(label):
    r = requests.get('{}?order=desc&sort=votes&tagged={}&site=stackoverflow'.format(base_url, label))
    if r.status_code == 200:
    	return r.json()
    else:
    	print('[!] Error HTTP {}'.format(r.status_code))
    	return None

n = int(sys.argv[1])
label = sys.argv[2]
data = get_faqs(label)

if data is not None:
    for question in data['items'][:n]:
	    print(question['title'])
	    print(question['link'] + '?answertab=votes#tab-top')
else:
	print('Most votes Q not found!')

