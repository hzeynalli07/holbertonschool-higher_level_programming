#!/usr/bin/python3
"""
This module defines a VerboseList class that extends the built-in list.
"""


class VerboseList(list):
    """A custom list that prints notifications on modifications."""

    def append(self, item):
        """Adds an item and prints a message."""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, items):
        """Extends the list and prints a message."""
        count = len(items)
        super().extend(items)
        print("Extended the list with [{}] items.".format(count))

    def remove(self, item):
        """Removes an item and prints a message."""
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Pops an item and prints a message."""
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)
