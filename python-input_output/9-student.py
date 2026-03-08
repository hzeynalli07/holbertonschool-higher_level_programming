#!/usr/bin/python3
"""Tələbə klasını təyin edən modul."""


class Student:
    """Tələbə məlumatlarını saxlayan klass."""

    def __init__(self, first_name, last_name, age):
        """İlkin dəyərləri təyin edir."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Obyektin lüğət təsvirini qaytarır."""
        return self.__dict__
