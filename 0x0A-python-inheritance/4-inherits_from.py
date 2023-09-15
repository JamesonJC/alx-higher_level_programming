#!/usr/bin/python3
'''Inheritens function checking on a class.'''


def inherits_from(obj, a_class):
    '''
    Checks if an object is an inherited instance of a class.

    Args:
        obj (any): Checked object.
        a_class (type): checked/matched class.

    Returns:
        True. if object is inherited instance of a class
        Otherwise - False.
    '''

    return issubclass(type(obj), a_class) and type(obj) != a_class
