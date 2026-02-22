#!/usr/bin/python3
"""
This module provides a function that divides all elements of a matrix.
It includes rigorous type checking for the matrix and the divisor.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor.

    Args:
        matrix: A list of lists of integers or floats.
        div: The number to divide by.

    Returns:
        A new matrix with values rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats,
                   or if rows have different sizes, or if div is not a number.
        ZeroDivisionError: If div is 0.
    """
    err_msg = "matrix must be a matrix (list of lists) of integers/floats"

    # Matrisin tipini yoxlayırıq
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(err_msg)

    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(err_msg)
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError(err_msg)

    # Sətirlərin ölçüsünü yoxlayırıq
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Divisor (div) yoxlaması
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Hesablama və yuvarlaqlaşdırma
    # Qeyd: float('inf') gələrsə, nəticə avtomatik 0.0 olacaq
    return [[round(x / div, 2) for x in row] for row in matrix]
