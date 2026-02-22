#!/usr/bin/python3
"""
This module provides a function that adds two integers.
The module contains one function: add_integer(a, b=98).
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats.

    Args:
        a: The first number, must be an integer or float.
        b: The second number, must be an integer or float. Default is 98.

    Returns:
        The integer sum of a and b.

    Raises:
        TypeError: If a or b are not integers or floats, or if they are NaN/Inf.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # NaN və Infinity yoxlaması (çünki int() bunları çevirə bilmir)
    if a != a or abs(a) == float('inf'):
        raise TypeError("a must be an integer")
    if b != b or abs(b) == float('inf'):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
