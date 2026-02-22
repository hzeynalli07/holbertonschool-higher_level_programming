#!/usr/bin/python3
"""
This module defines a class Square with size validation.
"""


class Square:
    """
    Defines a square by a private instance attribute size.
    """
    def __init__(self, size=0):
        """
        Initializes the square.

        Args:
            size (int): The size of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
