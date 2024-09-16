#!/usr/bin/python3
"""Module 2-square: défine a class Square with size validation"""


class Square:
    """Square class"""

    def __init__(self, size=0):

        if not isinstance(size, int):
            raise TypeError("Size must be an integer")

        if size < 0:
            raise ValueError("size must be >=0")

        self.__size = size

    def area(self):
        """Calculate and return area of square"""

        return self.__size ** 2
