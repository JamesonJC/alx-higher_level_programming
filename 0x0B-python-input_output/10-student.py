#!/usr/bin/python3
''' A class Student defination. '''


class Student:
    '''Class represantation of a student.'''

    def __init__(self, first_name, last_name, age):
        '''
        Constructer for Student class.

        Args:
            first_name (str): Student first name.
            last_name (str): Student last name.
            age (int): Student age.
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''
        Defines student in the form of a dictionary.

        Args:
            attrs (list): The attributes of the the class.
        '''
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
