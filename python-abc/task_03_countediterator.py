#!/usr/bin/python3
"""
This module defines a CountedIterator class that tracks the number
of items iterated over.
"""


class CountedIterator:
    """An iterator that keeps track of the count of items fetched."""

    def __init__(self, data):
        """Initializes the iterator and counter."""
        self.__iterator = iter(data)
        self.__counter = 0

    def get_count(self):
        """Returns the current value of the counter."""
        return self.__counter

    def __next__(self):
        """Increments the counter and fetches the next item."""
        try:
            item = next(self.__iterator)
            self.__counter += 1
            return item
        except StopIteration:
            raise StopIteration

    def __iter__(self):
        """Returns the iterator object itself."""
        return self
