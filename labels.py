#
# Really crude code to add my standard Issue Labels in Github
# 

from pathlib import Path
import requests

keyfile = f"{Path().home()}/.ghkey"

with open(keyfile) as f:
    api_key = f.readline().strip()

#print(api_key)

owner = "marekwolski"
repo = "fuel-price-checker"

url = f'https://api.github.com/repos/{owner}/{repo}/labels'
headers = {'Authorization': f'Bearer {api_key}'}

label_list = []
label_list.append({'name': 'next up', 'description': 'Do this issue next', 'color': 'D4C5F9'})
label_list.append({'name': 'bug', 'description': 'Something is not working', 'color': 'd73a4a'})
label_list.append({'name': 'enhancement', 'description': 'New feature or request', 'color': 'a2eeef'})
label_list.append({'name': 'spike', 'description': 'Exploring, investigating, just trying something', 'color': 'DAFE14'})
label_list.append({'name': 'in progress', 'description': 'Work is underway', 'color': '5319E7'})
label_list.append({'name': 'documentation', 'description': 'Improvements or additions to documentation', 'color': '0075ca'})
label_list.append({'name': 'epic', 'description': 'A big issue containing smaller ones', 'color': 'FBCA04'})

for new_label in label_list:

    #data = {'name': 'next up', 'description': 'Do this issue next', 'color': 'D4C5F9'}
    response = requests.post(url, headers=headers, json=new_label)

    if response.status_code == 201:
        print(f'Label {new_label["name"]} created successfully!')
    else:
        print(f'Error creating label {new_label["name"]}:', response.json())
        print(f'Error creating label {new_label["name"]}:', response.json()['message'])
