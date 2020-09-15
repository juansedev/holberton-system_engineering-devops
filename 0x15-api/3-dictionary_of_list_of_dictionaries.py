#!/usr/bin/python3
""" Script """

import json
import requests
from sys import argv

if __name__ == "__main__":
    # Get the user
    url = 'https://jsonplaceholder.typicode.com/users/'
    all_users = requests.get(url)

    # Get the tasks
    url = 'https://jsonplaceholder.typicode.com/todos'
    all_tasks = requests.get(url)

    dict_task = {}

    for user in all_users.json():
        list_task = []
        for task in all_tasks.json():
            if user.get('id') == task.get('userId'):
                t_dict = {"username": user['username'],
                          "task": task['title'],
                          "completed": task['completed']}
                list_task.append(t_dict)
        dict_task[user.get('id')] = list_task

    with open("todo_all_employees.json", mode='w') as my_file:
        json.dump(dict_task, my_file)
