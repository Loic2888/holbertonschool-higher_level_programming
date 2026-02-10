#!/usr/bin/python3
"""A function that reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout

    Args:
        filename (str, optional): The name of the file. Defaults to "".
    """
    with open(filename, "r") as f:
        print(f.read(), end="")
