#!/usr/bin/python3
"""
Shapes and Duck Typing with specific output format.
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract class Shape."""
    @abstractmethod
    def area(self):
        """Abstract method area."""
        pass

    @abstractmethod
    def perimeter(self):
        """Abstract method perimeter."""
        pass


class Circle(Shape):
    """Circle class."""
    def __init__(self, radius):
        """Initialize Circle."""
        self.radius = radius

    def area(self):
        """Return area."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Return perimeter."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle class."""
    def __init__(self, width, height):
        """Initialize Rectangle."""
        self.width = width
        self.height = height

    def area(self):
        """Return area."""
        return self.width * self.height

    def perimeter(self):
        """Return perimeter."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print shape info with potential inline format."""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
