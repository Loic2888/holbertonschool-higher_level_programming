#!/usr/bin/python3
"""
Demonstrates Python abstract base classes (ABC).

Features:
- Abstract Animal class with sound() method
- Concrete Dog and Cat subclasses
- Forces method implementation in subclasses
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract base class for animals.
    """

    @abstractmethod
    def sound(self):
        """Returns the animal's sound."""
        pass


class Dog(Animal):
    """Dog class implementing animal sound."""

    def sound(self):
        """Returns dog's bark sound."""
        return "Bark"


class Cat(Animal):
    """Cat class implementing animal sound."""

    def sound(self):
        """Returns cat's meow sound."""
        return "Meow"
