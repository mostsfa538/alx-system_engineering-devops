#!/usr/bin/python3
"""Export all employee TODOs to JSON format."""
import json
import requests

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'

    users = requests.get(url + "users").json()
    todos = requests.get(url + "todos").json()

    dataset = {}

    for user in users:
        user_id = user['id']
        username = user['username']
        user_tasks = [task for task in todos if task['userId'] == user_id]
        dataset[user_id] = [{
            "username": username,
            "task": task["title"],
            "completed": task["completed"]
        } for task in user_tasks]

    json_filename = 'todo_all_employees.json'
    with open(json_filename, 'w') as jsonfile:
        json.dump(dataset, jsonfile)
