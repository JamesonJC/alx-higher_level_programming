#!/usr/bin/python3

'''Defination of a class squre'''


class Square:
    '''square methods or attributes'''
    def __init__(self, size=0):
        ''' init square wit attribute size
        Args:
            size - Square size
        Raises:
            TypeError: if size is not an integer
            ValueError: if size is below zero
        '''
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

        def area(self)
        ''' computes the area of the sqare
        Returns: The results sqaring the value size
        '''
        return (self.__size ** 2)
