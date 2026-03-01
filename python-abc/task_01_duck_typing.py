#!/usr/bin/python3
"""
Shapes module with Circle, Rectangle and Shape classes.
"""
import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """Abstract class Shape."""

    @abstractmethod
    def area(self):
        """Calculate area."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate perimeter."""
        pass


class Circle(Shape):
    """Circle class."""

    def __init__(self, radius):
        """Initialize Circle."""
        self.radius = radius

    def area(self):
        """Return area of circle."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Return perimeter of circle."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle class."""

    def __init__(self, width, height):
        """Initialize Rectangle."""
        self.width = width
        self.height = height

    def area(self):
        """Return area of rectangle."""
        return float(self.width * self.height)

    def perimeter(self):
        """Return perimeter of rectangle."""
        return float(2 * (self.width + self.height))


def shape_info(shape):
    """Prints area and perimeter of a shape."""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
