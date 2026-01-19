#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if not tuple_a and not tuple_b:
        return (0, 0)
    if len(tuple_a) or len(tuple_b) > 2:
        tuple_a = tuple_a[:2]
        tuple_b = tuple_b[:2]
        while len(tuple_a) < 2:
            tuple_a += (0,)
        while len(tuple_b) < 2:
            tuple_b += (0,)
    else:
        tuple_a = (0, 0)
        tuple_b = (0, 0)
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
