#!/usr/bin/python3
"""5-save_to_json_file.py"""


import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using a JSON representation

    Args:
        my_obj: The object to be written to the file
        filename: The name of the file to which the object should be written
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
