#!/usr/bin/python3
"""4-inherits_from.py
"""

def inherits_from(obj, a_class):
    """ Check for direct or indirect inheritance """
    
    return isinstance(obj, a_class) and type(obj) != a_class
