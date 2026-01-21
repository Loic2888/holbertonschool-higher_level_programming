#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_table = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000}

    if roman_string is None or not isinstance(roman_string, str):
        return None
    total = 0
    for i in roman_string.upper():
        total += roman_table.get(i, 0)
    return total
