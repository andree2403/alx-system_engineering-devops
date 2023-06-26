import requests
import csv

response = requests.get('https://jsonplaceholder.typicode.com/users/1/todos').json()
print("{}".format(len(response)))
