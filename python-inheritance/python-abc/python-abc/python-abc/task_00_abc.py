#!/usr/bin/python3
"""
This module defines an abstract class Animal and its subclasses Dog and Cat.
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract class representing an animal."""

    @abstractmethod
    def sound(self):
        """Abstract method that must be implemented by subclasses."""
        pass


class Dog(Animal):
    """Subclass of Animal representing a dog."""

    def sound(self):
        """Returns Bark."""
        return "Bark"


class Cat(Animal):
    """Subclass of Animal representing a cat."""

    def sound(self):
        """Returns Meow."""
        return "Meow"
