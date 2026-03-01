#!/usr/bin/python3
"""
Module for Shape, Circle and Rectangle.
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
        """Init Circle"""
        self.radius = radius

    def area(self):
        """Area of Circle"""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Perimeter of Circle"""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle class"""
    def __init__(self, width, height):
        """Init Rectangle"""
        self.width = width
        self.height = height

    def area(self):
        """Area of Rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Perimeter of Rectangle"""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Prints area and perimeter of a shape"""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
