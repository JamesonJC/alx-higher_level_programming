#!/usr/bin/python3
'''Class defination'''


class Student:
    ''' A class student represenation. '''
    def __init__(self, first_name, last_name, age):
        '''
        Constructor for a new Student.

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
        Define dictionary representation of the student.

        Args:
            attrs (list): The attributes of the student class.

        Returns:
            dict: A student in the for of dictionary.

        '''
        if attrs is None:
            return self.__dict__
        return {
            attr: getattr(self, attr, None)
            for attr in attrs
            if hasattr(self, attr)
        }

    def reload_from_json(self, json):
        '''
        Replaces all attributes with a dictionary value.

        Args:
            json (dict): Key/values to use for replacing.

        '''
        for key, value in json.items():
            setattr(self, key, value)
