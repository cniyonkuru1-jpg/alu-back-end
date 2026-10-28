#!/usr/bin/python3
"""Display the completed TODO tasks for one employee."""

import requests
import sys


API_URL = "https://jsonplaceholder.typicode.com"


def main():
    """Fetch and print the TODO progress for one employee."""
    if len(sys.argv) != 2:
        return

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        return

    employee = requests.get("{}/users/{}".format(
        API_URL, employee_id)).json()
    tasks = requests.get("{}/todos?userId={}".format(
        API_URL, employee_id)).json()

    employee_name = employee.get("name", "")
    completed_tasks = [task for task in tasks if task.get("completed")]
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, len(completed_tasks), len(tasks)))
    for task in completed_tasks:
        print("\t {}".format(task.get("title", "")))


if __name__ == "__main__":
    main()
