#!/usr/bin/python3
"""
Shapes and Duck Typing
"""
import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """Abstract class Shape"""

    @abstractmethod
    def area(self):
        """Abstract method area"""
        pass

    @abstractmethod
    def perimeter(self):
        """Abstract method perimeter"""
        pass


class Circle(Shape):
    """Circle class"""

    def __init__(self, radius):
        """Initialize Circle"""
        self.radius = radius

    def area(self):
        """Return circle area"""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Return circle perimeter"""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle class"""

    def __init__(self, width, height):
        """Initialize Rectangle"""
        self.width = width
        self.height = height

    def area(self):
        """Return rectangle area"""
        return self.width * self.height

    def perimeter(self):
        """Return rectangle perimeter"""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print shape info"""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
