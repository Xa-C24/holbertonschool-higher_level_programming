#!/usr/bin/python3
"""
    This module check the inheritance of an object
"""


def inherits_from(obj, a_class):
    """ Check for direct or indirect inheritance """
    return isinstance(obj, a_class) and type(obj) is not a_class
