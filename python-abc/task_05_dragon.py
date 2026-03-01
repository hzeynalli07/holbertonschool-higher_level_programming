#!/usr/bin/python3
"""
This module demonstrates Mixins with SwimMixin, FlyMixin, and Dragon classes.
"""


class SwimMixin:
    """Mixin that provides swimming functionality."""
    def swim(self):
        """Prints swimming message."""
        print("The creature swims!")


class FlyMixin:
    """Mixin that provides flying functionality."""
    def fly(self):
        """Prints flying message."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon class that inherits from both SwimMixin and FlyMixin."""
    def roar(self):
        """Prints dragon roaring message."""
        print("The dragon roars!")
