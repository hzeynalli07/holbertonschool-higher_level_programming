#!/usr/bin/python3
"""Mətn faylını oxumaq üçün funksiyanı təyin edir."""


def read_file(filename=""):
    """UTF8 formatlı mətn faylını oxuyur və stdout-a çap edir."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
