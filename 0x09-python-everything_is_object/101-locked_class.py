#!/usr/bin/python3
'''Defination of a LockedClass class.'''


class LockedClass:
    '''LockedClass represenation.
    Attributes:
    __slots__: List of strings serving as valid attribute
               identifiers as in `self.__dict__`.
    '''
    __slots__ = ['first_name']
