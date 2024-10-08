#!/usr/bin/python3
"""
This module defines a Square class that inherits from Rectangle.
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ inherits from Rectangle class """

    def __init__(self, size):
        """
        Initializes Square class which inherits from Rectangle.

        Args:
            Size (int): The size of the square
        """

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ Returns area of Square object"""

        return self.__size ** 2
