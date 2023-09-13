#!/usr/bin/python3
''' JSON representation of Python object to a text file
'''
import json


def save_to_json_file(my_obj, filename):
    '''
    Function of text file of a JSON representaion of Python.

    Args:
        my_obj: JSON representation to be converted.
        filename: file to write text in.

    return:
          Text file
    '''

    with open(filename, 'w') as file:
        file.write(json.dumps(my_obj))
