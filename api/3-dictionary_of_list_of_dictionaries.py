#!/usr/bin/python3
"""Export TODO tasks for all employees to JSON."""

import json
from urllib.error import HTTPError, URLError
from urllib.request import urlopen


API_URL = "https://jsonplaceholder.typicode.com"


def get_json(url):
    """Return decoded JSON from a URL."""
    with urlopen(url) as response:
        return json.loads(response.read().decode("utf-8"))


def main():
    """Fetch all employees and their tasks and write a JSON file."""
    try:
        employees = get_json("{}/users".format(API_URL))
        tasks = get_json("{}/todos".format(API_URL))
    except (HTTPError, URLError, ValueError):
        return

    if not isinstance(employees, list) or not isinstance(tasks, list):
        return

    users = {}
    for employee in employees:
        employee_id = employee.get("id")
        if employee_id is not None:
            users[str(employee_id)] = []

    for task in tasks:
        employee_id = str(task.get("userId", ""))
        if employee_id in users:
            employee = next(
                item for item in employees
                if str(item.get("id", "")) == employee_id
            )
            users[employee_id].append({
                "username": employee.get("username", ""),
                "task": task.get("title", ""),
                "completed": task.get("completed", False)
            })

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(users, json_file, indent=2)
        json_file.write("\n")


if __name__ == "__main__":
    main()
