#!/usr/bin/python3
"""Module with MyList class that inherits from list"""


class MyList(list):
    """class that inherits from list"""
    def print_sorted(self):
        """Prints list in sorted ascending order."""
        print(sorted(self))
