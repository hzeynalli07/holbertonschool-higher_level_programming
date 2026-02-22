#!/usr/bin/python3
"""
This module provides a function that adds two integers.
The function ensures that the inputs are either integers or floats.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats after casting them to integers.

    Args:
        a: The first number (int or float).
        b: The second number (int or float), defaults to 98.

    Returns:
        The integer sum of a and b.

    Raises:
        TypeError: If a or b are not integers or floats, or are NaN.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # NaN və ya Infinity yoxlaması üçün float metodu istifadə edirik
    try:
        a = int(a)
    except (ValueError, OverflowError):
        raise TypeError("a must be an integer")

    try:
        b = int(b)
    except (ValueError, OverflowError):
        raise TypeError("b must be an integer")

    return a + b
