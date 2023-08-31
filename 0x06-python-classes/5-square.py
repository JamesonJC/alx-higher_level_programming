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

    def area(self):
        ''' Computes the square area
            Returns: results of squaring size value
        '''
        return (self.__size ** 2)

    @property
    def size(self):
        '''Retrieve square size'''
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        '''
        Computes square area for size
        Returns: results of squaring size value
        '''
        return (self.__size ** 2)

    def my_print(self):
        '''prints out the square with # '''
        if self.__size == 0:
            print()
        for i in range(self.__size):
            print("#" * self.__size)
