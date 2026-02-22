#!/usr/bin/python3
"""
This module provides a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor.

    Args:
        matrix: A list of lists of integers or floats.
        div: The number to divide by (integer or float).

    Returns:
        A new matrix with the results rounded to 2 decimal places.

    Raises:
        TypeError: If the matrix is not a list of lists of integers/floats.
        TypeError: If rows of the matrix are not the same size.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is 0.
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"

    # Matris və daxilindəki siyahıların yoxlanılması
    if not isinstance(matrix, list) or not matrix or not matrix[0]:
        raise TypeError(msg)

    row_len = len(matrix[0])

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(msg)
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError(msg)

    # Divisor (div) yoxlanılması
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Yeni matrisin yaradılması (List Comprehension)
    return [[round(x / div, 2) for x in row] for row in matrix]
