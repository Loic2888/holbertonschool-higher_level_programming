#!/usr/bin/python3
"""Defines a Student class."""


class Student:
    """Defines a student."""
    def __init__(self, first_name, last_name, age):
        """Instantiate a Student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dict representation of the Student.
        If attrs is a list of strings, only attributes with those
        names are included; otherwise, all attributes are returned.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
