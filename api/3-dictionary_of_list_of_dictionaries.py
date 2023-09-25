#!/usr/bin/python3
""" This module defines the REST API """
import json
import requests

if __name__ == "__main__":
    api = "https://jsonplaceholder.typicode.com"
    users = requests.get(api + "/users").json()
    all_todos = {}

    for user in users:
        user_id = user['id']
        todos = requests.get(api + "/todos", params={"userId": user_id}).json()
        user_todos = [{"username": user["username"], "task": todo["title"],
                       "completed": todo["completed"]} for todo in todos]
        all_todos[user_id] = user_todos

    with open("todo_all_employees.json", "w") as outfile:
        json.dump(all_todos, outfile)
