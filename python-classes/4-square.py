#!/usr/bin/python3
"""This module defines a class Square with size validation, getter, and setter."""


class Square:
    """Square class"""

    def __init__(self, size=0):

        self.size = size

    @property
    def size(self):
        """Getter for the size attribute."""

        return self.__size

    @size.setter
    def size(self, value):
        """Setter for the size attribute."""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return area of square"""

        return self.__size ** 2

