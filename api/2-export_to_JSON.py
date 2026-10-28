#!/usr/bin/python3
"""Export all TODO tasks for one employee to JSON."""

import json
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
    records = []

    for task in tasks:
        records.append({"task": task.get("title"),
                        "completed": task.get("completed"),
                        "username": employee.get("username")})

    with open("{}.json".format(employee_id), "w") as json_file:
        json.dump({employee_id: records}, json_file)
