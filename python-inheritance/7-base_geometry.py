#!/usr/bin/python3
"""
    This module defines a class BaseGeometry.

    Class:
        BaseGeometry: Class representing the basic geometry with an 'area'

    Methods:
        area(self): Raises an exception if called.

"""


class BaseGeometry:
    """class BaseGeometry with an area method."""

    def area(self):
        """
        Raises an Exception indicating that the area method is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that 'value' is an integer and greater than 0.

        Args:
            name (str): The name of the parameter (always a string).
            value (int): The value to be validated.

        Raises:
            TypeError: If 'value' is not an integer.
            ValueError: If 'value' is less than or equal to 0.
        """

        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
