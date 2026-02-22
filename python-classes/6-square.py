#!/usr/bin/python3
"""
This module defines a class Square with size, position, and printing logic.
"""


class Square:
    """
    Defines a square by size and position.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes the square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter for size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter for position."""
        return self.__size_position

    @position.setter
    def position(self, value):
        """Setter for position with validation."""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size_position = value

    def area(self):
        """Calculates area."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with position consideration."""
        if self.__size == 0:
            print("")
            return

        # Yuxarıdan buraxılan boş sətirlər (position[1])
        for _ in range(self.__size_position[1]):
            print("")

        # Kvadratın özü
        for _ in range(self.__size):
            # Soldan buraxılan boşluqlar (position[0]) + # simvolları
            print(" " * self.__size_position[0] + "#" * self.__size)
