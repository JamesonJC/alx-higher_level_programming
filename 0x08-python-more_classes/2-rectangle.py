#!/usr/bin/python3
'''

A  Rectangle

'''


class Rectangle:
    """ Rectangle represantations """
    def __init__(self, width=0, height=0):
        ''' Method to initializes instances(constructor)

        Args:
            width: rectangle width
            height: rectangle height

        '''
        self.width = width
        self.height = height

    @property
    def width(self):
        ''' method retrieves the width

        Returns:
            value rectangle width

        '''
        return (self.__width)

    @width.setter
    def width(self, value):
        ''' method set the value of width

        Args:
            value: width

        Raises:
            TypeError: if width is not an integer
            ValueError: if width is less than zero

        '''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

        @property
        def height(self):
            ''' method retrieves the height

            Returns:
                value rectangle height

            '''
            return (self.__height)

        @height.setter
        def height(self, value):
            ''' method set the value of height

            Args:
                value: height

            Raises:
                TypeError: if height is not an integer
                ValueError: if height is less than zero


            '''

            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be >= 0")
            self.__height = value

        def area(self):
            ''' Method working the area of the rectangle

            Returns:
                Value rectangle area

            '''
            return (self.width * self.height)

        def perimeter(self):
            ''' Method working the perimeter of the rectangle

            Returns:
                Value rectangle perimeter

            '''
            if self.height == 0 or self.width == 0:
                return (0)

            return ((2 * self.height) + (2 * self.width))
