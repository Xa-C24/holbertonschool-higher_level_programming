#!/usr/bin/python3

class MyList(list):
    """"
    Class that inherits from the list class and adds a print_sorted method.
    """

    def print_sorted(self):
        """
        Imprime la liste triée (en ordre croissant) sans la modifier.
        """
        print(sorted(self))
