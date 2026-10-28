#!/usr/bin/python3
"""Export all employees' TODO tasks to JSON."""

import json
import requests


if __name__ == "__main__":
    employees = requests.get(
        "https://jsonplaceholder.typicode.com/users").json()
    tasks = requests.get(
        "https://jsonplaceholder.typicode.com/todos").json()
    records = {}

    for employee in employees:
        employee_id = employee.get("id")
        records[str(employee_id)] = []
        for task in tasks:
            if task.get("userId") == employee_id:
                records[str(employee_id)].append({
                    "username": employee.get("username"),
                    "task": task.get("title"),
                    "completed": task.get("completed")
                })

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(records, json_file)
