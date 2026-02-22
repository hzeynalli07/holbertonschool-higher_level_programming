#!/usr/bin/python3
"""
This module provides a function that adds 2 integers.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats.
    Args:
        a: first integer
        b: second integer
    Returns:
        Addition of a and b
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    # NaN və Infinity yoxlamasını ən sadə yolla edirik:
    # Onlar integer-ə çevrilə bilmədiyi üçün bu halda da TypeError fırlanmalıdır.
    if a != a or a == float('inf') or a == float('-inf'):
        raise TypeError("a must be an integer")
    if b != b or b == float('inf') or b == float('-inf'):
        raise TypeError("b must be an integer")

    # Şərtə uyğun olaraq: ÖNCƏ integer-ə cast edirik, SONRA toplayırıq
    a = int(a)
    b = int(b)

    return (a + b)
