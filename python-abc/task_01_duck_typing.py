#!/usr/bin/python3
"""
This module defines an abstract class Shape and its subclasses Circle and Rectangle.
It also includes a function shape_info to demonstrate duck typing.
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract class Shape with area and perimeter abstract methods."""

    @abstractmethod
    def area(self):
        """Abstract method to calculate the area of a shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Abstract method to calculate the perimeter of a shape."""
        pass


class Circle(Shape):
    """Circle class that inherits from Shape."""

    def __init__(self, radius):
        """Initialize Circle with a radius."""
        self.radius = radius

    def area(self):
        """Calculate and return the area of the circle."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Calculate and return the perimeter of the circle."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle class that inherits from Shape."""

    def __init__(self, width, height):
        """Initialize Rectangle with width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print the area and perimeter of any object with area and perimeter methods."""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
