#!/usr/bin/python3
"""
This module defines a function called lookup
"""

def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Args:
        obj: The object to retrieve the attributes and methods from.

    Returns:
        A list of strings representing the available attributes and methods.
    """

    return dir(obj)
