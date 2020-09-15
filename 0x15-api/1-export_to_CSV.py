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

    with open("{}.csv".format(user_id), mode='w') as my_file:
        for task in task_li.json():
            my_file.write('"{}","{}","{}","{}"\n'.format(user_id,
                                                         user_name,
                                                         task['completed'],
                                                         task['title']))
