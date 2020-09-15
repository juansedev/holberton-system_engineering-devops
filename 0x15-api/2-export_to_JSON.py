#!/usr/bin/python3
""" Script """

import json
import requests
from sys import argv


if __name__ == "__main__":
    user_id = argv[1]
    # Get the user
    url = 'https://jsonplaceholder.typicode.com/users/' + user_id
    user = requests.get(url)
    user_name = user.json().get('username')

    # Get the task
    url = 'https://jsonplaceholder.typicode.com/users/' + user_id + '/todos'
    task_li = requests.get(url)

    dict_task = {}
    list_task = []

    for task in task_li.json():
        t_dict = {"task": task['title'],
                  "completed": task['completed'],
                  "username": user_name}
        list_task.append(t_dict)
    dict_task[user_id] = list_task

    with open("{}.json".format(user_id), mode='w') as my_file:
        json.dump(dict_task, my_file)
