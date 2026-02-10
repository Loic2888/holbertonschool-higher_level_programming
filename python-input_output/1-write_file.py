#!/usr/bin/python3
"""A function that writes a string to a text file
 (UTF8) and returns the number of characters written"""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8) and returns the number of characters written
    Args:
        filename (str, optional): The name of the file. Defaults to "".
        text (str, optional): The string to write to the file. Defaults to "".
    Returns:
        int: The number of characters written
    """
    with open(filename, "w") as f:
        f.write(text)
    return len(text)
