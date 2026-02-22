#!/usr/bin/python3
"""
This module provides a function `print_square(size)` that prints a square
using the `#` character.
"""


def print_square(size):
    """
    Prints a square with the character #.

    Args:
        size: The length of the side of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
        TypeError: If size is a float and less than 0.
    """
    # Xüsusi hal: Əgər float-dırsa və mənfidirsə, TypeError fırlanmalıdır
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
