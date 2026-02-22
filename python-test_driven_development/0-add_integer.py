#!/usr/bin/python3
"""
This module provides a function that adds two integers.
It handles edge cases like infinity and NaN by catching internal errors.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats.

    Args:
        a: The first number.
        b: The second number (default 98).

    Returns:
        The sum as an integer.

    Raises:
        TypeError: If a or b are not integers or floats, or cannot be cast.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    try:
        # Cast əməliyyatını try bloku daxilində edirik.
        # Əgər NaN və ya Infinity gələrsə, Python burada xəta fırladacaq.
        a = int(a)
    except (ValueError, OverflowError):
        raise TypeError("a must be an integer")

    try:
        b = int(b)
    except (ValueError, OverflowError):
        raise TypeError("b must be an integer")

    return a + b
