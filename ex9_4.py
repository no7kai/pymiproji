import requests
import json
import time

base_url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/'


def nearby_search(coordinate, radius, token):
	api_url = '{}json?location={}&radius={}&type=bar&key={}'.format(base_url,coordinate,radius,token)
	r1 = requests.get(api_url)
	if r1.status_code == 200:
		page1 = r1.json()
		next_token1 = page1['next_page_token']
		time.sleep(3)
		r2 = requests.get(api_url + '&pagetoken={}'.format(next_token1))
		page2 = r2.json()
		next_token2 = page2['next_page_token']
		time.sleep(3)
		r3 = requests.get(api_url + '&pagetoken={}'.format(next_token2))
		page3 = r3.json()
		data = {"type": "FeatureCollection", "features": []}
		for page in page1, page2, page3:
			for info in page['results']:
				if len(data["features"]) < 50:
					coor = [info["geometry"]["location"]["lng"],info["geometry"]["location"]["lat"]]
					geoPoint = {"type": "Feature", "geometry": {"type": "Point", "coordinates": coor}, "properties": {"Address": info["vicinity"], "name": info["name"]}}
					data["features"].append(geoPoint)
		with open('pymi_bar.geojson', 'w') as f:
			json.dump(data, f, ensure_ascii=False, indent=2)
		print("File pymi_bar.geojson has been created. Please upload to Github to see map results.")
	else:
		print('[!] Erro HTTP {}'.format(r1.status_code))

coordinate = '21.021645,105.792128'
radius = str(2000)
with open('ggAPIkey.txt') as f:
	token = f.readline()
nearby_search(coordinate, radius, token)