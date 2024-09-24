#!/usr/bin/python3
"""
This module defines a class MyList that inherits from the built-in list class
and provides an additional method to print the list in sorted order.
"""


class MyList(list):
    """"
    Class that inherits from the list class and adds a print_sorted method.
    """

    def print_sorted(self):
        """
        Imprime la liste triée (en ordre croissant) sans la modifier.
        """
        print(sorted(self))
