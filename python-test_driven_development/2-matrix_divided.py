#!/usr/bin/python3
"""
Docstring for 2-matrix_divided
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor.

    Args:
        matrix (list): A list of lists of integers or floats.
        div (int/float): The number to divide by.

    Returns:
        list: A new matrix with the result of the division.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats.
        TypeError: If each row of the matrix is not of the same size.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is 0.
    """

    # 1. Validate Matrix Type (Must be list of lists of ints/floats)
    type_error_msg = "matrix must be a matrix of integers/floats"

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(type_error_msg)

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(type_error_msg)
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError(type_error_msg)

    # 2. Validate Row Sizes (Must be consistent)
    size_error_msg = "Each row of the matrix must have the same size"

    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError(size_error_msg)

    # 3. Validate Divisor Type (Must be number)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # 4. Validate Divisor Value (Cannot be zero)
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # 5. Perform Division and Return New Matrix
    # Using list comprehension to create a new matrix with rounded values
    new_matrix = [[round(x / div, 2) for x in row] for row in matrix]

    return new_matrix
