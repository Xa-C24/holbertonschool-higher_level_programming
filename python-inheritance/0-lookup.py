#!/usr/bin/python3
"""
This module defines a function called lookup
"""

def lookup(obj):
    """
        Returns a list of the attributes and methods available for an object.
    """
    return dir(obj)
