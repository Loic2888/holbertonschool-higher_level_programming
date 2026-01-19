#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    first = sentence[0]
    if not sentence:
        length = 0
        first = None
    return length, first
