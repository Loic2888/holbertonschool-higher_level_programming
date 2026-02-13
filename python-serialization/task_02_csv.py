#!/usr/bin/env python3
"""
Module task_02_csv
Converts CSV data to JSON format.
"""

import csv
import json


def convert_csv_to_json(csv_filename):
    """Convert CSV file to JSON and write to 'data.json'.
    Args:
        csv_filename (str): Path to input CSV file.
    Returns:
        bool: True if successful, False on exceptions
        (e.g., file not found).
    """
    try:
        with open(csv_filename, 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = list(csv_reader)
        with open('data.json', 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file)
        return True

    except (FileNotFoundError, csv.Error, json.JSONDecodeError, IOError):
        return False
