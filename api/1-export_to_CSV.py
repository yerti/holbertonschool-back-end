#!/usr/bin/python3
"""This module defines the REST API"""
import csv
import requests
import sys

if __name__ == '__main__':
    api = "https://jsonplaceholder.typicode.com"
    user = requests.get(api + "/users/{}".format(sys.argv[1])).json()
    todos = requests.get(api + "/todos", params={"userId": sys.argv[1]}).json()
    name = "{}.csv".format(user["id"])

    with open(name, mode="w", newline="") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

        for todo in todos:
            writer.writerow([user["id"], user["username"],
                            str(todo["completed"]), todo["title"]])
