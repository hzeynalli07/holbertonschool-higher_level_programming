#!/usr/bin/python3
"""
Module for Shape, Circle, Rectangle and shape_info.
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
    """Class Circle."""

    def __init__(self, radius):
        """Initializes radius."""
        self.radius = radius

    def area(self):
        """Calculates area."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Calculates perimeter."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Class Rectangle."""

    def __init__(self, width, height):
        """Initializes width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Calculates area."""
        return self.width * self.height

    def perimeter(self):
        """Calculates perimeter."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Duck typing shape_info."""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
