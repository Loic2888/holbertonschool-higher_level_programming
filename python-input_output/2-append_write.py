#!/usr/bin/python3
"""Script that appends a string to a text file"""


def append_write(filename="", text=""):
    """Function that appends a string to a text file and
    returns the characters written"""
    with open(filename, "a", encoding="UTF-8") as f:
        return f.write(text)
