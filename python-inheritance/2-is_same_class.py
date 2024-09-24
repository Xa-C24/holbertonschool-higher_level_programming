#!/usr/bin/python3
def is_same_class(obj, a_class):
    """
    This module define  a function that checks if an object is exactly
    an instance of a specified class.
    
    Returns True if the object is exactly an instance of the specified class, otherwise False.
    """
    return type(obj) == a_class
