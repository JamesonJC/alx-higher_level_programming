#!/usr/bin/python3
''' Function that returns the JSON representation of an object (string)'''

import json


def to_json_string(my_obj):
    '''
    Function  convert the given object to its JSON represention.

    Args:
        my_obj: Object to be converted.

    Returns:
        JSON representation.

    '''
    return (json.dumps(my_obj))
