#!/usr/bin/python3
"""
    This module defines a class BaseGeometry with methods for area calculation and integer validation.
    
    Class:
        BaseGeometry: Class representing the basic geometry with an 'area' method
    
    Methods:
        area(self): Raises an exception
    
    """
class BaseGeometry:
    """class BaseGeometry with an area method."""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
