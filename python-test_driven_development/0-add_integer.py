#!/usr/bin/python3
"""
This module provides a function that adds two integers.
Check for type, infinity and NaN before casting.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats.

    Args:
        a: first number
        b: second number, defaults to 98

    Returns:
        The addition of a and b as an integer
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    # NaN və Infinity yoxlaması - casting-dən əvvəl
    # (a * 0 != 0) yoxlaması həm NaN, həm də Inf-i eyni anda tutur!
    try:
        if a * 0 != 0:
            raise TypeError("a must be an integer")
    except (ValueError, OverflowError):
        raise TypeError("a must be an integer")

    try:
        if b * 0 != 0:
            raise TypeError("b must be an integer")
    except (ValueError, OverflowError):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
