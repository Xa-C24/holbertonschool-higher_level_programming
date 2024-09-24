#!/usr/bin/python3
"""10-square.py
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class which inherits from Rectangle."""

    def __init__(self, size):
        """Initialise the square with a size."""
        if self.integer_validator("size", size)
            self.__size = size
        super().__init__(size, size)

    def area(self):
        """Returns the area of the square."""
        return self.__size ** 2
