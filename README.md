# API

This directory contains Python scripts that retrieve employee TODO data from
the JSONPlaceholder REST API and report or export it.

## Requirements

- Python 3
- Network access to `https://jsonplaceholder.typicode.com`

## Usage

Run the scripts from the `api` directory:

```sh
python3 0-gather_data_from_an_API.py EMPLOYEE_ID
python3 1-export_to_CSV.py EMPLOYEE_ID
python3 2-export_to_JSON.py EMPLOYEE_ID
python3 3-dictionary_of_list_of_dictionaries.py
```

The export scripts create `EMPLOYEE_ID.csv`, `EMPLOYEE_ID.json`, and
`todo_all_employees.json` in the current directory.
