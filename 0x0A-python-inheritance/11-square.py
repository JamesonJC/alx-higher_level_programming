#!/usr/bin/python3

'''A Rectangle subclass Square.'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''Defination of a square class.'''

    def __init__(self, size):
        '''Constructor of a new square object.

        Args:
            size (int): square size.
        '''
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
