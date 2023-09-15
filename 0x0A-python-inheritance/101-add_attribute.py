#!/usr/bin/python3
'''A function adds attributes to an objects.'''


def add_attribute(obj, att, value):
    '''
    add_attribute function defination.

    Args:
        obj (any): objected added attribute.
        att (str): attribute to add.
        value (any): attribute value.

    Raises:
        TypeError: If the attribute cannot be added.
    '''
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
