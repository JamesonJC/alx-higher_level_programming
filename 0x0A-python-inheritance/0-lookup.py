#!/usr/bin/python3
'''Lookup function defination.'''


def lookup(obj):
    '''
    Returns a list of an object's available attributes.
    Args:
        obj (object): The object to look up atrributes.

    Return:
        list: A list of attributes

    '''
    return (dir(obj))
