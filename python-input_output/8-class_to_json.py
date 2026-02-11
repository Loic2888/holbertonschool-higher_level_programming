#!/usr/bin/python3
"""8-class_to_json.py"""


def class_to_json(obj):
    """Returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean) for JSON serialization of an object
    Args:
        obj: The object to convert to a dictionary
    Returns:
        The dictionary description of the object for JSON serialization
    """
    return obj.__dict__
