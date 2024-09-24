#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    """
    This module define a function that checks if an object.
    
    Args:
         obj: The object to be checked.
         a_class: The class to compare with the type of obj.
    
    Returns True if the object is an instance of the specified class 
    or of a class which inherits from it.
    """
    return isinstance(obj, a_class)
 