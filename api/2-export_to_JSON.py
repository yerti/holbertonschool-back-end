#!/usr/bin/python3
""" This module defines the REST API """
import json
import requests
import sys

if __name__ == "__main__":
    api = "https://jsonplaceholder.typicode.com"
    user_id = sys.argv[1]
    user = requests.get(api + "/users/{}".format(user_id)).json()
    todos = requests.get(api + "/todos", params={"userId": user_id}).json()

    user_todos = [{"task": todo["title"], "completed": todo["completed"],
                   "username": user["username"]} for todo in todos]

    output_data = {user_id: user_todos}

    with open(f"{user_id}.json", "w") as outfile:
        json.dump(output_data, outfile)
