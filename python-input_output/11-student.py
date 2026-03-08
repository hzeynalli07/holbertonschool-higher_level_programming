#!/usr/bin/python3
"""Yenilənə bilən Tələbə klası."""


class Student:
    """Tələbə məlumatlarını saxlayan və yeniləyən klass."""

    def __init__(self, first_name, last_name, age):
        """İlkin dəyərləri təyin edir."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Obyektin lüğət təsvirini qaytarır."""
        if isinstance(attrs, list) and all(isinstance(s, str) for s in attrs):
            res = {}
            for k in attrs:
                if k in self.__dict__:
                    res[k] = self.__dict__[k]
            return res
        return self.__dict__

    def reload_from_json(self, json):
        """Lüğətdəki bütün açarları obyektin atributları ilə əvəz edir."""
        for key, value in json.items():
            setattr(self, key, value)
