#!/usr/bin/python3
"""Define a class Square based on 3-square.py."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new Square."""
        self.size = size

    @property
    def size(self):
        """Getter for the private size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for the private size attribute."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return self.__size ** 2
