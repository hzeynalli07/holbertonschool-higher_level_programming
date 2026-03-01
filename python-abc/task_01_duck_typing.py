#!/usr/bin/python3
"""
Shapes and Duck Typing
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract class Shape"""
    @abstractmethod
    def area(self):
        """Abstract method for area"""
        pass

    @abstractmethod
    def perimeter(self):
        """Abstract method for perimeter"""
        pass


class Circle(Shape):
    """Circle class"""
    def __init__(self, radius):
        """Initialize Circle"""
        self.radius = radius

    def area(self):
        """Calculate area of circle"""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Calculate perimeter of circle"""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle class"""
    def __init__(self, width, height):
        """Initialize Rectangle"""
        self.width = width
        self.height = height

    def area(self):
        """Calculate area of rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Calculate perimeter of rectangle"""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print shape information using duck typing"""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
