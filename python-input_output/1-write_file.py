#!/usr/bin/python3
"""Fayla yazı yazmaq üçün funksiyanı təyin edir."""


def write_file(filename="", text=""):
    """Mətni UTF8 formatında fayla yazır və simvol sayını qaytarır."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
