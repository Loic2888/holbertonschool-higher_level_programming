#!/usr/bin/python3
"""define a class"""


class MyList(list):
    """class that inherits from list"""
    def print_sorted(self):
        """Prints list in sorted ascending order."""
        print(sorted(self))
