# API

Python scripts that retrieve employee TODO data from the JSONPlaceholder REST
API and present it in several formats.

## Files

- `0-gather_data_from_an_API.py` prints an employee's completed TODO tasks.
- `1-export_to_CSV.py` writes an employee's TODO tasks to `USER_ID.csv`.
- `2-export_to_JSON.py` writes an employee's TODO tasks to `USER_ID.json`.
- `3-dictionary_of_list_of_dictionaries.py` writes every employee's TODO tasks
  to `todo_all_employees.json`.

## Usage

Run a single-employee script with an employee ID:

```sh
python3 0-gather_data_from_an_API.py 2
python3 1-export_to_CSV.py 2
python3 2-export_to_JSON.py 2
```

Export all employees' tasks with:

```sh
python3 3-dictionary_of_list_of_dictionaries.py
```

The scripts use `https://jsonplaceholder.typicode.com` as their data source.
