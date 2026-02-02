#!/usr/bin/python3
"""define a class"""


class MyList(list):
    """class that inherits from list"""
    def print_sorted(self):
        print(sorted(self))
