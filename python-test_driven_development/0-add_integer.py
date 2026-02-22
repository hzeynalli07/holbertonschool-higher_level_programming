#!/usr/bin/python3
"""
This module provides a function that adds two integers.
Validation is performed to handle floats, infinity, and NaN values.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats after casting them to integers.

    Args:
        a: The first number.
        b: The second number (default 98).

    Returns:
        The sum as an integer.

    Raises:
        TypeError: If a or b are not integers, floats, or are NaN/Inf.
    """
    # Tip yoxlaması
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # NaN yoxlaması (a != a yalnız NaN üçün True-dur)
    if a != a:
        raise TypeError("a must be an integer")
    if b != b:
        raise TypeError("b must be an integer")

    # Infinity (sonsuzluq) yoxlaması
    if a == float('inf') or a == float('-inf'):
        raise TypeError("a must be an integer")
    if b == float('inf') or b == float('-inf'):
        raise TypeError("b must be an integer")

    # Bütün yoxlamalardan keçdikdən sonra int-ə çeviririk
    return int(a) + int(b)
