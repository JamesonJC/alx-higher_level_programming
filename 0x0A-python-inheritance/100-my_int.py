#!/usr/bin/python3
'''A class MyInt that is inherited from int.'''


class MyInt(int):
    '''Class MyInt Defination.'''

    def __eq__(self, value):
        '''Override == opeartor with != behavior.'''
        return self.real != value

    def __ne__(self, value):
        '''Override != operator with == behavior.'''
        return self.real == value
