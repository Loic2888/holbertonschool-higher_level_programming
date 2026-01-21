#!/usr/bin/python3
def safe_print_integer(value):
    try:
        nombre = int(value)
        print("{:d}".format(nombre))
        return True
    except ValueError:
        return False
