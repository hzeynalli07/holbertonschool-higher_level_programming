#!/usr/bin/python3
"""
Module for Shape, Circle and Rectangle classes.
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
    """Circle class inheriting from Shape"""
    def __init__(self, radius):
        """Initializes Circle with radius"""
        self.radius = radius

    def area(self):
        """Returns the area of the circle"""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Returns the perimeter of the circle"""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle class inheriting from Shape"""
    def __init__(self, width, height):
        """Initializes Rectangle with width and height"""
        self.width = width
        self.height = height

    def area(self):
        """Returns the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Prints the area and perimeter of a given shape"""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
