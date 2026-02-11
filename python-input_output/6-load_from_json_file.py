#!/usr/bin/python3
"""6-load_from_json_file.py"""


import json


def load_from_json_file(filename):
    """Creates an Object from a “JSON file”
    Args:
        filename: The name of the file to read from
    Returns:
        The object represented by the JSON string in the file
    """
    with open(filename, 'r') as f:
        return json.load(f)
