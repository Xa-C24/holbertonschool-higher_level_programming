#!/usr/bin/python3
""" 
    This module define a function which checks whether an object
    is an instance of a class that inherits from the specified class.

    Args:
        obj: The object to be checked.
        a_class: The reference class for the comparison.

    Returns:
        True if the object is an instance of a class the specified class,
        but not if the object is a direct instance of the specified class.
    """
def inherits_from(obj, a_class):
    
    return isinstance(obj, a_class) and type(obj) != a_class
