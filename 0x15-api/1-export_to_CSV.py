#!/usr/bin/python3
""" Here goes every thing """
import csv
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

    tasksData = []

    for task in tasks:
        data = {}
        data['ID'] = int(id)
        data['Name'] = emp_name
        data['Status'] = task[1]
        data['task'] = task[0]

        tasksData.append(data)

    with open(f'{id}.csv', 'w') as csvfile:
        fieldnames = tasksData[0].keys()

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames,
                                quoting=csv.QUOTE_ALL)

        for row in tasksData:
            writer.writerow(row)
