#!/usr/bin/python3
'''A Rectangle subclass Square.'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''Defination of a class square.'''

    def __init__(self, size):
        '''constructor for a new object square.

        Args:
            size (int): Square size.
        '''
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
