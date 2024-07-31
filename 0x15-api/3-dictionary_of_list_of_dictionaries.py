#!/usr/bin/python3
"""Python script to fetch REST API for todo
lists of employees and save them in JSON format
"""

import json
import requests
import sys


def fetch_data(url):
    """Fetch data from the given URL and return the JSON response"""
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        sys.exit(1)


if __name__ == '__main__':
    base_url = "https://jsonplaceholder.typicode.com/users"
    users = fetch_data(base_url)

    all_tasks = {}
    for user in users:
        user_id = user.get('id')
        username = user.get('username')
        todos_url = f"{base_url}/{user_id}/todos"
        tasks = fetch_data(todos_url)

        all_tasks[user_id] = []
        for task in tasks:
            task_info = {
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": username
            }
            all_tasks[user_id].append(task_info)

    output_file = 'todo_all_employees.json'
    try:
        with open(output_file, 'w') as json_file:
            json.dump(all_tasks, json_file, indent=4)
    except IOError as e:
        print(f"Error writing to file {output_file}: {e}")
        sys.exit(1)
