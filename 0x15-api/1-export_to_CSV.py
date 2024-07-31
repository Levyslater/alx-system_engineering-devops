#!/usr/bin/python3
""" Extend your Python script to export data in the CSV format """

import csv
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

    url_user = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    try:
        res_user = requests.get(url_user)
        res_user.raise_for_status()
    except requests.RequestException as e:
        print(f"Error: Unable to fetch user data: {e}")
        sys.exit(1)

    user_data = res_user.json()
    username = user_data.get('username')

    if not username:
        print(f"Error: User with ID {user_id} not found")
        sys.exit(1)

    url_tasks = f'{url_user}/todos'
    try:
        res_tasks = requests.get(url_tasks)
        res_tasks.raise_for_status()
    except requests.RequestException as e:
        print(f"Error: Unable to fetch tasks data: {e}")
        sys.exit(1)

    tasks = res_tasks.json()

    csv_filename = f'{user_id}.csv'
    try:
        with open(csv_filename, mode='w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
            for task in tasks:
                csv_writer.writerow([user_id, username,
                                    task.get('completed'), task.get('title')])
    except IOError as e:
        print(f"Error: Unable to write to file {csv_filename}: {e}")
        sys.exit(1)
