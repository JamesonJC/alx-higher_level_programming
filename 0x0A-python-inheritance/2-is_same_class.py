#!/usr/bin/python3
'''A Function that checks a class.'''


def is_same_class(obj, a_class):
    '''
    is_same_class - checks for an object if is an instance of a given class.

    Args:
        obj (any): Object to check.
        a_class (type): Given class.

    Returns:
        True. if ojects matches the class
        Otherwise - False.
    '''
    return type(obj) == a_class
