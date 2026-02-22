#!/usr/bin/python3
"""
This module provides a function that adds two integers.
The inputs must be integers or floats.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats after casting them to integers.

    Args:
        a: The first number.
        b: The second number, defaults to 98.

    Returns:
        The integer sum of a and b.

    Raises:
        TypeError: If a or b are not integers or floats.
    """
    # Birinci tip yoxlaması
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # NaN və Infinity yoxlaması (Float overflow və NaN xətalarını tutmaq üçün)
    # Əgər rəqəmdirsə, mütləq özü-özünə bərabər olmalı və sonlu olmalıdır
    if a != a or a == float('inf') or a == float('-inf'):
        raise TypeError("a must be an integer")
    if b != b or b == float('inf') or b == float('-inf'):
        raise TypeError("b must be an integer")

    # Əgər bura qədər gəlibsə, deməli təhlükəsizdir
    return int(a) + int(b)
