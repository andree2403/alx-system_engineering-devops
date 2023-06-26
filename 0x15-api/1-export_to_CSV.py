#!/usr/bin/python3
""" returns in csv format"""
import csv
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()
    completed_task = [[sys.argv[1], user.get('name'), item.get('completed'),
                      item.get('title')] for item in todos]

    filename = '{}.csv'.format(sys.argv[1])

    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        writer.writerows(completed_task)
