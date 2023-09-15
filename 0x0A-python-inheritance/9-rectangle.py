#!/usr/bin/python3
'''A class Rectangle inherited from BaseGeometry.'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Representation of a rectangle using BaseGeometry.'''

    def __init__(self, width, height):
        '''Contructor for a new Rectangle.

        Args:
            width (int): Rectangle width.
            height (int): Rectangle height.
        '''
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        '''Returns area.'''
        return self.__width * self.__height

    def __str__(self):
        '''Returns print() and str() representation of a Rectangle.'''
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
