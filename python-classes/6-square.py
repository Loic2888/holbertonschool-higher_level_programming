#!/usr/bin/python3
"""define a square like 5-square"""


class Square:
    """Represent a square."""
    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square.
        
        Args:
            size (int): Size of the square.
            position (tuple): Position of the square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter for the private size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for the private size attribute.
        
        Args:
            value (int): New size value.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter for the position attribute."""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for the position attribute.
        
        Args:
            value (tuple): New position tuple.
        """
        if (not isinstance(value, tuple) or
            len(value) != 2 or
            not isinstance(value[0], int) or
            not isinstance(value[1], int) or
            value[0] < 0 or
            value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with '#' using position."""
        if self.__size == 0:
            print("")
            return
        for i in range(self.__position[1]):
            print("")
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
