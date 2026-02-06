#!/usr/bin/python3
"""
Demonstrates abstract Shape class with Circle and Rectangle implementations.
Includes shape_info function for polymorphism testing.
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for geometric shapes."""

    @abstractmethod
    def area(self):
        """Calculates and returns the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculates and returns the perimeter of the shape."""
        pass


class Circle(Shape):
    """Circle shape with radius."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Returns circle area: π * r²."""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Returns circle circumference: 2 * π * r."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle shape with width and height."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """Returns rectangle area: width * height."""
        return self.width * self.height

    def perimeter(self):
        """Returns rectangle perimeter: 2 * (width + height)."""
        return 2 * (self.width + self.height)


def shape_info(shape: Shape):
    """Prints area and perimeter of any Shape object."""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
