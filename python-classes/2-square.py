#!/usr/bin/python3
"""Define a class Square based on 2-square.py."""


class Square:
    """define a classe square, init it and raise error"""
    def __init__(self, size=0):
        """Initialize a new Square."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
