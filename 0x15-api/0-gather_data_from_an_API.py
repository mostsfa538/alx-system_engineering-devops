#!/usr/bin/python3
""" Here goes every thing """
import requests
import sys


if __name__ == '__main__':
    id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user_response = requests.get(url + f"users/{id}").json()
    todo_response = requests.get(url + f"todo").json()

    todo_response = [
        task for task in todo_response if task['userId'] == int(id)]
    emp_name = user_response['name']
    total_tasks = len(todo_response)
    tasks = [task['title']
             for task in todo_response if task['completed'] is True]

    print(
        f'Employee {emp_name} is done with tasks({len(tasks)}/{total_tasks}):')
    for task in tasks:
        print(f'\t {task}')
