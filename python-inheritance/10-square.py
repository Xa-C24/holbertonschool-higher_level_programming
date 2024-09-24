#!/usr/bin/python3
"""10-square.py
This module defines a Square class that inherits from Rectangle.
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    
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
        """
        Returns the area of the square.
        
        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
