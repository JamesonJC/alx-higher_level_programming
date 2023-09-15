#!/usr/bin/python3
'''A class Rectangle that inherited from BaseGeometry.'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Representation of a rectangle using BaseGeometry.'''

    def __init__(self, width, height):
        ''' constructor for a new Rectangle object.

        Args:
            width (int): Rectangle with
            height (int): Rectangle height.

        '''

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
