#!/usr/bin/python3
"""
Module for is_kind_of_class function.
Contains a function that returns True if the object is an instance of,
or if the object is an instance of a class that inherited from,
the specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if obj is an instance of a_class or its subclasses.

    Args:
        obj: The object to check.
        a_class: The class to match against.

    Returns:
        True if it's an instance or inherited, otherwise False.
    """
    return isinstance(obj, a_class)
