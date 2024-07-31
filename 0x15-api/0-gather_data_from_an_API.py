#!/usr/bin/python3
'''
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
'''

import requests
import sys

REST_API = "https://jsonplaceholder.typicode.com"


def get_employee_data(employee_id):
    """Fetch employee data and tasks from the REST API"""
    user_url = f'{REST_API}/users/{employee_id}'
    todos_url = f'{REST_API}/todos?userId={employee_id}'

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    if user_response.status_code != 200 or todos_response.status_code != 200:
        print(f"Error: Unable to fetch data for employee ID {employee_id}")
        sys.exit(1)

    user_data = user_response.json()
    todos_data = todos_response.json()

    return user_data, todos_data


def display_todo_progress(employee_name, todos):
    """Display TODO list progress for the employee"""
    completed_tasks = [task for task in todos if task['completed']]
    total_tasks = len(todos)
    completed_tasks_count = len(completed_tasks)

    print(f'Employee {employee_name} is done with tasks(
            {completed_tasks_count}/{total_tasks}): ')
    for task in completed_tasks:
        print(f'\t {task["title"]}')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: ./script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: Employee ID must be an integer")
        sys.exit(1)

    employee_data, todos = get_employee_data(employee_id)

    if 'name' not in employee_data:
        print(f"Error: No employee found with ID {employee_id}")
        sys.exit(1)

    employee_name = employee_data['name']
    display_todo_progress(employee_name, todos)
