#!/usr/bin/python3
"""Export all TODO tasks for one employee to CSV."""

import csv
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

    with open("{}.csv".format(employee_id), "w", newline="") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in tasks:
            writer.writerow([employee_id, employee.get("username"),
                             task.get("completed"), task.get("title")])
