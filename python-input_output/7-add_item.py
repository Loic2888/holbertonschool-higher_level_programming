#!/usr/bin/python3
"""7-add_item.py"""


import json
import sys


load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


file = "add_item.json"
my_obj = load_from_json_file(file)
my_obj.extend(sys.argv[1:])
save_to_json_file(my_obj, file)
