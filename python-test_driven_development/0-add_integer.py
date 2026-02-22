#!/usr/bin/python3
"""
This module provides a function that adds two integers.
The inputs must be integers or floats, otherwise a TypeError is raised.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats after casting them to integers.

    Args:
        a: The first number (int or float).
        b: The second number (int or float).

    Returns:
        The sum of a and b as an integer.

    Raises:
        TypeError: If a or b are not integers or floats, or are NaN/Inf.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # NaN və Infinity yoxlaması
    # NaN özü-özünə bərabər olmayan yeganə dəyərdir (a != a)
    if a != a or a == float('inf') or a == float('-inf'):
        raise TypeError("a must be an integer")
    if b != b or b == float('inf') or b == float('-inf'):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
