#!/usr/bin/python3
"""
script that returns the user and a list
of total tasks and completed tasks
"""


import requests
import sys


API = 'https://jsonplaceholder.typicode.com'


endpoints = {
        "users": f"{API}/users", # https://jsonplaceholder.typicode.com/users
        "todos": f"{API}/todos" # https://jsonplaceholder.typicode.com/todos
        }

def get_todo_list_progress(employee_id: int) -> str:
    """
    We get the employee with id employee_id
    """
    get_employee_endpoint = f"{endpoints['users']}/{employee_id}" # https://jsonplaceholder.typicode.com/users/1
    employee_response = requests.get(get_employee_endpoint)
    employee = employee_response.json()

    """
    We get the list of tasks of the employee with id employee_id
    """
    get_employee_todos_endpoint = f"{endpoints['todos']}?userId={employee_id}" # https://jsonplaceholder.typicode.com/todos?userId=1
    todos_response = requests.get(get_employee_todos_endpoint)
    todos = todos_response.json()

    todos_quantity = len(todos)

    """
    We filter the tasks to get the list of completed and uncompleted tasks
    """
    completed_todos = []

    for todo in todos:
        if todo["completed"] == True:
            completed_todos.append(todo)
    completed_todos_quantity = len(completed_todos)

    first_line = f"Employee {employee['name']} is done with tasks({completed_todos_quantity}/{todos_quantity}):\n"

    next_line = ''
    for completed_todo in completed_todos:
        next_line = next_line + "\t " + completed_todo["title"] + "\n"

    return first_line + next_line

employee_id = sys.argv[1]

output = get_todo_list_progress(employee_id)

print(output)
