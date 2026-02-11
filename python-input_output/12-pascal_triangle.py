#!/usr/bin/python3
"""12-pascal_triangle.py"""


def pascal_triangle(n):
    """Return a list of lists representing Pascal's triangle of n."""
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        row = [1]

        if i > 0:
            prev = triangle[i - 1]
            for j in range(1, i):
                row.append(prev[j - 1] + prev[j])
            if i > 0:
                row.append(1)
        triangle.append(row)

    return triangle
