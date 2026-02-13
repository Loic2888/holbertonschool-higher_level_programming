#!/usr/bin/env python3
"""
Module task_00_basic_serialization
Provides functions to serialize Python dict to JSON
file and deserialize back.
"""


import json


def serialize_and_save_to_file(data, filename):
    """Serialize a Python Dictionary to JSON and
    save to the specified file.
    Args:
        data (dict): Python Dictionary with data to serialize.
        filename (str): The filename of the output JSON file.
    Replaces existing file if it exists.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Load and deserialize JSON data from the specified file.
    Args:
        filename (str): The filename of the input JSON file.
    Returns:
        dict: Python Dictionary with the deserialized JSON data.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
