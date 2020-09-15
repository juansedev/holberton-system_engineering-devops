#!/usr/bin/python3
""" Script """

import requests
from sys import argv


if __name__ == "__main__":
    user_id = argv[1]
    # Get the user
    url = 'https://jsonplaceholder.typicode.com/users/' + user_id
    user = requests.get(url)
    user_name = user.json().get('name')

    # Get the task
    url = 'https://jsonplaceholder.typicode.com/users/' + user_id + '/todos'
    task_li = requests.get(url)
    task_done = [task for task in task_li.json() if task['completed'] is True]

    len_don = len(task_done)
    len_all = len(task_li.json())
    print("Employee {} is done with tasks({}/{}):".format(user_name,
                                                          len_don,
                                                          len_all))

    for task in task_done:
        print('\t ' + task['title'])
