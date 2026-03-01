#!/usr/bin/python3
"""
Module for Abstract Base Class (ABC) task.
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract class Animal"""

    @abstractmethod
    def sound(self):
        """Abstract method for sound"""
        pass


class Dog(Animal):
    """Subclass Dog that inherits from Animal"""

    def sound(self):
        """Returns Bark"""
        return "Bark"


class Cat(Animal):
    """Subclass Cat that inherits from Animal"""

    def sound(self):
        """Returns Meow"""
        return "Meow"
