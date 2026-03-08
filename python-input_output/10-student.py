#!/usr/bin/python3
"""Filtrləmə qabiliyyəti olan Tələbə klası."""


class Student:
    """Tələbə məlumatlarını saxlayan klass."""

    def __init__(self, first_name, last_name, age):
        """İlkin dəyərləri təyin edir."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Obyektin lüğət təsvirini (istəyə bağlı filtrlə) qaytarır."""
        if isinstance(attrs, list) and all(isinstance(s, str) for s in attrs):
            res = {}
            for k in attrs:
                if k in self.__dict__:
                    res[k] = self.__dict__[k]
            return res
        return self.__dict__
