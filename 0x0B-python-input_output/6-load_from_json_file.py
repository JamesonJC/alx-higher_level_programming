#!/usr/bin/python3
'''Function to load data from a JSON file.'''
import json


def load_data_from_json_file(filename):
    '''
    Load data from a JSON file and return it as a Python object.

    Args:
        filename (str): The name of the JSON file to read.

    Returns:
        dict or list: The Python object representing the JSON data.
    '''
    with open(filename) as file:
        data = json.load(file)
        return (data)

