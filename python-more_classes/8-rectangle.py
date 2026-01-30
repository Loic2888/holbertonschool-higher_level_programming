#!/usr/bin/python3
"""define a rectangle class"""


class Rectangle:
    """Defines a rectangle."""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Initialize a new rectangle.

        :param width: initial width of the rectangle (int >= 0, default 0)
        :param height: initial height of the rectangle (int >= 0, default 0)
        :raises TypeError: if width or height is not an integer
        :raises ValueError: if width or height is negative
        Incrémente le compteur d'instances lors de la création.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Width property (read-only access).

        :getter: Returns the current width of the rectangle
        :setter: Sets the width (must be int >= 0)
        :type: int
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the rectangle's width.

        :param value: new width (int >= 0)
        :raises TypeError: if value is not an integer
        :raises ValueError: if value is negative
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Height property (read-only access).

        :getter: Returns the current height of the rectangle
        :setter: Sets the height (must be int >= 0)
        :type: int
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the rectangle's height.

        :param value: new height (int >= 0)
        :raises TypeError: if value is not an integer
        :raises ValueError: if value is negative
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculate and return the area of the rectangle.

        :return: area (width * height)
        :rtype: int
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculate and return the perimeter of the rectangle.

        Returns 0 if either width or height is 0 (degenerate rectangle).

        :return: perimeter (2 * (width + height)) or 0 if degenerate
        :rtype: int
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width + self.__height) * 2

    def __str__(self):
        """Return the rectangle with the character print_symbol."""
        if self.__width == 0 or self.__height == 0:
            return ""
        result = ""
        for i in range(self.__height):
            for j in range(self.__width):
                result += str(self.print_symbol)
            if i != self.__height - 1:
                result += "\n"
        return result

        def __repr__(self):
        """Return a string to recreate the rectangle."""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """
        Destructor method called when the Rectangle instance is deleted.
        Prints a farewell message to indicate the object's destruction.
        Triggered automatically by Python's garbage collector
        or explicit 'del' statement.
        Décrémente le compteur d'instances.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Return the biggest rectangle based on the area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
