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

    todos = [task for task in todo if task['userId'] == int(id)]
    emp_name = user['username']

    completed_tasks = len([task for task in todos if task['completed']])
    total_tasks = len(todos)

    print(f'Employee {emp_name} is done with tasks({completed_tasks}/{total_tasks}):')
    for task in todos:
        if task['completed']:
            print(f'\t {task["title"]}')

    dataset = []

    for task in todos:
        data = {
            "ID": id,
            "Name": emp_name,
            "Status": str(task["completed"]),
            "task": task["title"]
        }
        dataset.append(data)

    csv_filename = f'{id}.csv'
    with open(csv_filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        for row in dataset:
            writer.writerow(
                [row["ID"], row["Name"], row["Status"], row["task"]])
