#!/usr/bin/python3
"""Display an employee's completed TODO tasks."""

import json
import sys
from urllib.error import HTTPError, URLError
from urllib.request import urlopen


API_URL = "https://jsonplaceholder.typicode.com"


def get_json(url):
    """Return decoded JSON from a URL."""
    with urlopen(url) as response:
        return json.loads(response.read().decode("utf-8"))


def main():
    """Fetch and print an employee's TODO progress."""
    if len(sys.argv) != 2:
        return

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        return

    try:
        employee = get_json("{}/users/{}".format(API_URL, employee_id))
        tasks = get_json("{}/todos?userId={}".format(API_URL, employee_id))
    except (HTTPError, URLError, ValueError):
        return

    if not isinstance(employee, dict) or not isinstance(tasks, list):
        return

    employee_name = employee.get("name", "")
    completed_tasks = [task for task in tasks if task.get("completed")]
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, len(completed_tasks), len(tasks)))
    for task in completed_tasks:
        print("\t {}".format(task.get("title", "")))


if __name__ == "__main__":
    main()
