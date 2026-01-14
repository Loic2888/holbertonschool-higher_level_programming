#!/usr/bin/python3
def uppercase(str):
    result = []
    for c in str:
        if 'a' <= c <= 'z':
            result.append(chr(ord(c) - 32))
        else:
            result.append(c)
    print("".join(result))
