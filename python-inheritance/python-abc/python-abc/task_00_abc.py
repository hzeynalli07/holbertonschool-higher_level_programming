#!/usr/bin/python3
"""
This module defines an abstract class Animal and its subclasses Dog and Cat.
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract class Animal."""

    @abstractmethod
    def sound(self):
        """Abstract method sound."""
        pass


class Dog(Animal):
    """Subclass Dog."""

    def sound(self):
        """Returns Bark."""
        return "Bark"


class Cat(Animal):
    """Subclass Cat."""

    def sound(self):
        """Returns Meow."""
        return "Meow"
