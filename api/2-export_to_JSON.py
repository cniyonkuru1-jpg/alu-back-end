#!/usr/bin/python3
"""Export one employee's TODO tasks to JSON."""

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
    """Fetch an employee's tasks and write the required JSON file."""
    if len(sys.argv) != 2:
        return

    try:
        employee_id = int(sys.argv[1])
        employee = get_json("{}/users/{}".format(API_URL, employee_id))
        tasks = get_json("{}/todos?userId={}".format(API_URL, employee_id))
    except (ValueError, HTTPError, URLError):
        return

    if not isinstance(employee, dict) or not isinstance(tasks, list):
        return

    username = employee.get("username", "")
    records = [{
        "task": task.get("title", ""),
        "completed": task.get("completed", False),
        "username": username
    } for task in tasks]

    with open("{}.json".format(employee_id), "w") as json_file:
        json.dump({str(employee_id): records}, json_file, indent=2)
        json_file.write("\n")


if __name__ == "__main__":
    main()
