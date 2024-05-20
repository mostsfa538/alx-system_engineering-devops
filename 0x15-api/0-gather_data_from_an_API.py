#!/usr/bin/python3
""" Here goes every thing """
import requests
from sys import argv


if __name__ == "__main__":
    id = argv[1]
    url = 'https://jsonplaceholder.typicode.com/'
    user = requests.get(url + f"users/{id}").json()
    todo = requests.get(url + f"todos").json()

    todo = [task for task in todo if task['userId'] == int(id)]
    emp_name = user['name']
    total_tasks = len(todo)
    tasks = [task['title'] for task in todo if task['completed'] is True]

    print(
        f'Employee {emp_name} is done with tasks({len(tasks)}/{total_tasks}):')
    for task in tasks:
        print(f'\t {task}')
