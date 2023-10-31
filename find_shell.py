#
# Starter code to get data from Shell
# and print "local" station data
#
import requests
import json

url = 'https://www.shell.co.uk/fuel-prices-data.html'
response = requests.get(url)
data = json.loads(response.text)

print(f"Last Updated: {data['last_updated']}")
for i in data['stations']:
    if i['postcode'].startswith('SK'):
        print(i['address'], i['prices']['E10'])
    if i['postcode'].startswith('WA16'):
        print(i['address'], i['prices']['E10'])

