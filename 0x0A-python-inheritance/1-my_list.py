#!/usr/bin/python3

''' MyList class representation. '''


class MyLIst(list):
    ''' 
    A subclass of class MyList with added method for printing the list.

    Attributes:
        No attributes added.

    Methods:
        print_sorted():
            print the list arranged/or sorted.


    '''
    def __int__(self):
        ''' Constructor for an empty Mylist Object. '''
        super().__init__()

    def print_sorted(self):
        '''
        Print sorted elements of the list.
        Args:
            None.
        Returns:
            None.

        '''
        sorted_list = sorted(self)
        print(sorted_lis)
