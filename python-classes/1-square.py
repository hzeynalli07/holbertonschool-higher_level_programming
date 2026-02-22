#!/usr/bin/python3
"""
This module defines a class Square with a private size attribute.
"""


class Square:
    """
    Defines a square by a private instance attribute size.
    """
    def __init__(self, size):
        """
        Initializes the square.

        Args:
            size: The size of the square.
        """
        self.__size = size
