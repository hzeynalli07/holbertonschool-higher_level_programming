#!/usr/bin/python3
"""
This module provides a function that adds two integers.
Validation is done strictly before any type casting to prevent overflow.
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
        TypeError: If a or b are not integers, floats, or are invalid numbers.
    """
    # 1. Tip yoxlaması (isinstance bəzən yetərli olmaya bilər, type istifadə edək)
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    # 2. NaN və Infinity yoxlaması (HEÇ BİR riyazi əməliyyat etmədən)
    # Rəqəmi string-ə çevirib yoxlamaq ən qəti yoldur, çünki casting xətası vermir
    if str(a) in ["nan", "inf", "-inf"]:
        raise TypeError("a must be an integer")
    if str(b) in ["nan", "inf", "-inf"]:
        raise TypeError("b must be an integer")

    # 3. Yalnız indi casting edirik
    a_int = int(a)
    b_int = int(b)

    return a_int + b_int
