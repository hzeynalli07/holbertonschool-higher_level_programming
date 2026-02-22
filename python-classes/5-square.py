#!/usr/bin/python3
"""
This module defines a class Square with a print method.
"""


class Square:
    """
    Defines a square by size, area calculation, and printing.
    """
    def __init__(self, size=0):
        """
        Initializes the square.

        Args:
            size (int): The size of the square.
        """
        self.size = size

    @property
    def size(self):
        """
        Getter for size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for size with validation.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with the character #.
        If size is 0, prints an empty line.
        """
        if self.__size == 0:
            print("")
            return

        for i in range(self.__size):
            print("#" * self.__size)
