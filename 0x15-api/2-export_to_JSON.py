#!/usr/bin/python3
""" Python script to get data from an API and convert it to JSON """

import json
import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: ./script.py <employee_id>")
        sys.exit(1)

    try:
        user_id = int(sys.argv[1])
    except ValueError:
        print("Error: Employee ID must be an integer")
        sys.exit(1)

    url_to_user = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    try:
        res_user = requests.get(url_to_user)
        res_user.raise_for_status()
    except requests.RequestException as e:
        print(f"Error: Unable to fetch user data: {e}")
        sys.exit(1)

    user_data = res_user.json()
    username = user_data.get('username')

    if not username:
        print(f"Error: User with ID {user_id} not found")
        sys.exit(1)

    url_to_task = f'{url_to_user}/todos'
    try:
        res_tasks = requests.get(url_to_task)
        res_tasks.raise_for_status()
    except requests.RequestException as e:
        print(f"Error: Unable to fetch tasks data: {e}")
        sys.exit(1)

    tasks = res_tasks.json()

    dict_data = {user_id: []}
    for task in tasks:
        task_completed_status = task.get('completed')
        task_title = task.get('title')
        dict_data[user_id].append({
            "task": task_title,
            "completed": task_completed_status,
            "username": username
        })

    json_filename = f'{user_id}.json'
    try:
        with open(json_filename, 'w') as json_file:
            json.dump(dict_data, json_file, indent=4)
    except IOError as e:
        print(f"Error: Unable to write to file {json_filename}: {e}")
        sys.exit(1)
