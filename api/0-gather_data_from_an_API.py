#!/usr/bin/python3
"""Display an employee's completed TODO tasks from a REST API."""

import requests
import sys

if __name__ == "__main__":
    employee_id = sys.argv[1]
    employee = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(
            employee_id)).json()
    tasks = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(
            employee_id)).json()
    completed = [task for task in tasks if task.get("completed")]

    print("Employee {} is done with tasks({}/{}):".format(
        employee.get("name"), len(completed), len(tasks)))
    for task in completed:
        print("\t {}".format(task.get("title")))
