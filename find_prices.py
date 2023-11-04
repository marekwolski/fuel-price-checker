#
# Starter code to get data
# and print "local" station data
#
# Example JSON: 'stations' object: {'site_id': 'gcqrpd6prjsg', 'brand': 'SHELL', 'address': 'MANCHESTER ROAD', 'postcode': 'SK10 2JJ', 'location': {'latitude': 53.275353, 'longitude': -2.128294}, 'prices': {'B7': 166.9, 'E10': 159.9}}
import requests, json
from retailers import retailers_list

#
# First attempts
#

url = 'https://www.shell.co.uk/fuel-prices-data.html'
response = requests.get(url)
data = json.loads(response.text)

print(f"SHELL: Last Updated: {data['last_updated']}")
for i in data['stations']:
    if i['postcode'].startswith('SK'):
        print(i['brand'], i['address'], i['prices']['E10'])
    if i['postcode'].startswith('WA16'):
        print(i['brand'], i['address'], i['prices']['E10'])

print()

url = 'https://www.bp.com/en_gb/united-kingdom/home/fuelprices/fuel_prices_data.json'
response = requests.get(url)
data = json.loads(response.text)

print(f"BP: Last Updated: {data['last_updated']}")
for i in data['stations']:
    if i['postcode'].startswith('SK'):
        print(i['brand'], i['address'], i['prices']['E10'])
    if i['postcode'].startswith('WA16'):
        print(i['brand'], i['address'], i['prices']['E10'])

# -------------------------------------------------------------




areas = {"SK10", "SK11", "WA16"}

for i in retailers_list:
    print('Getting:', i['name'], i['url'])
    response = requests.get(i['url'])
    data = json.loads(response.text)

    print(f"{i['name']}: Last Updated: {data['last_updated']}")
    for i in data['stations']:
        if i.get('postcode') != None:
            p = i['postcode'].split()
            if p[0] in areas:
                print('------', i['brand'], i['address'], i['prices']['E10'])


