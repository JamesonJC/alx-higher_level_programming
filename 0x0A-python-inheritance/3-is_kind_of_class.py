#!/usr/bin/python3
'''a_class defination and is_kind_of_class function representations.'''


def is_kind_of_class(obj, a_class):
    '''
    If an object is an instance or inherited instance of a class.

    Args:
        obj (any): Object checked
        a_class (type): Class matched to object.

    Returns:
        True. if object is na instance or inherited instance of a class.
        Otherwise - False.
    '''
    return (isinstance(obj, a_class))
