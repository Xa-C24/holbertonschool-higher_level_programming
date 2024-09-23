#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of the specified class or of a class which inherits from it.
    """
    return isinstance(obj, a_class)
 