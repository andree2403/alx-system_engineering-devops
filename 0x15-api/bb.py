import requests
import csv

response = requests.get('https://jsonplaceholder.typicode.com/users/').json()
for r in response:
    print(r['id'])
