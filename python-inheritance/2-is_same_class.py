#!/usr/bin/python3
"""
    This module defines check if object is exactly one instance
"""


def is_same_class(obj, a_class):
    """ Compare if obj is exactly an instance of a_class """
    return type(obj) is a_class
