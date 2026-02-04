#!/usr/bin/python3
"""Module that defines the inherits_from function."""


def is_kind_of_class(obj, a_class):
    """Function that returns True if the object is an instance of a class
    that is or inherited (directly or indirectly) from the specified class;"""
    return issubclass(type(obj), a_class)
