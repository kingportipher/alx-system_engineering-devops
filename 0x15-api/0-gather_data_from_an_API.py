#!/usr/bin/python3
"""
Returns to-do list information for a given employee ID.

"""

import requests
import sys

if __name__ == "__main__":
    # Base URL for the JSONPlaceholder API
    url = "https://jsonplaceholder.typicode.com/"

    # Ensure correct number of command-line arguments
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    # Get the employee information using the provided employee ID
    employee_id = sys.argv[1]
    user_response = requests.get(f"{url}users/{employee_id}")
    user_data = user_response.json()

    # Get the to-do list for the employee using the provided employee ID
    todo_response = requests.get(f"{url}todos?userId={employee_id}")
    todo_data = todo_response.json()

    # Filter completed tasks and count them
    completed_tasks = [todo['title'] for todo in todo_data if todo['completed']]

    # Print the employee's name and the number of completed tasks
    total_tasks = len(todo_data)
    print(f"Employee {user_data['name']} is done with tasks ({len(completed_tasks)}/{total_tasks}):")

    # Print the completed tasks one by one with indentation
    for task in completed_tasks:
        print(f"\t{task}")
