#!/usr/bin/python3
'''Function to load data from a JSON file.'''
import json


def load_data_from_json_file(filename):
    '''
    load_data_from_json_file: Load data from a JSON file
    and return it as a Python object.

    Args:
        filename (str): The name of the JSON file to read.

    Returns:
         dict or list: The Python object representing the JSON data.
    '''

    with open(filename, "r") as file:
        try:
            data = json.load(file)
            return data
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            return None


if __name__ == "__main__":
    filename = "your_json_file.json"  # Replace with the actual JSON file path
    loaded_data = load_data_from_json_file(filename)

    if loaded_data is not None:
        print(loaded_data)
