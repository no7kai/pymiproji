import requests
import sys
from bs4 import BeautifulSoup


def get_results():
    r = requests.get('http://ketqua.net/')
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, features='html.parser')
        table = soup.find('table', attrs={'id': 'result_tab_mb'})
        results = table.findAll('td', attrs={'class': 'phoi-size'})
        list_result = []
        for result in results:
            list_result.append(result.text[-2:])
        return list_result
    else:
    	print('[!] Error HTTP {}'.format(r.status_code))
    	return None

results = get_results()
your_lotos = sys.argv[1:]
match = []

if results is not None:
    for loto in your_lotos:
	    if loto[-2:] in results:
		    match.append(loto)
    if match == []:
	    ketqua = ' '.join(results)
	    print('Ban da xit lo. Ket qua hom nay:', ketqua)
    else:
	    ketqua = ' '.join(match)
	    print('Chuc mung ban da trung lo con:', ketqua)
else:
	print('Khong lay duoc ket qua hom nay')