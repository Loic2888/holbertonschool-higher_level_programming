#!/usr/bin/python3
"""
Docstring for 0-add_integer
"""


def add_integer(a, b=98):
    """
    Docstring for add_integer
    :param a: First integer to sum
    :param b: Second integer to sum
    """
    try:
        if a is None:
            raise TypeError("a must be an integer")
        if type(a) is not int and type(a) is not float:
            raise TypeError("a must be an integer")
        if type(b) is not int and type(b) is not float:
            raise TypeError("b must be an integer")
        a = int(a)
        b = int(b)
        return a + b
    except SyntaxError:
        raise SyntaxError
