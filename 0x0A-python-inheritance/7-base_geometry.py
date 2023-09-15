#!/usr/bin/python3
''' Empty class BaseGeometry representation. '''


class BaseGeometry:
    '''Defination of a base geometry.'''

    def area(self):
        '''Defination of area, not implemented'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''
        Checks if a parameter is an integer or not.

        Args:
            name (str): Parameter name.
            value (int): Integer to be checked.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.

        '''
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
