#!/usr/bin/python3
"""A function that returns the JSON representation of an object (string)"""


import json


def from_json_string(my_str):
    """Return the Python object representation of a JSON string."""
    return json.loads(my_str)
