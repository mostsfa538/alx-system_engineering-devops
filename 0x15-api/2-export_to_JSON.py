#!/usr/bin/python3
""" Here goes everything """
import json
import requests
from sys import argv

if __name__ == "__main__":
    id = argv[1]
    url = 'https://jsonplaceholder.typicode.com/'
    user = requests.get(url + f"users/{id}").json()
    todo = requests.get(url + f"todos").json()

    todos = [task for task in todo if task['userId'] == int(id)]
    emp_name = user['username']

    completed_tasks = len([task for task in todos if task['completed']])
    total_tasks = len(todos)

    print(
        f'Employee {emp_name} is done with tasks({completed_tasks}/{total_tasks}):')
    for task in todos:
        if task['completed']:
            print(f'\t {task["title"]}')

    dataset = {id: []}

    for task in todos:
        data = {
            "task": task["title"],
            "completed": task["completed"],
            "username": emp_name
        }
        dataset[id].append(data)

    json_filename = f'{id}.json'
    with open(json_filename, 'w') as jsonfile:
        json.dump(dataset, jsonfile)
