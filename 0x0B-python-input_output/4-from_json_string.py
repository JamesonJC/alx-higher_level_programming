#!/usr/bin/python3
'''Returns a Python data structure represention by JSON string'''

import json


def from_json_string(my_str):
    '''
    converts the given JSON tp Python data structure.

    Args:
         my_str (str):

    Returns:
        object: Python data representation.

    '''
    return json.loads(my_str)
